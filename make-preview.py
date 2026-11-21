from pathlib import Path
import re,json,base64,zipfile
root=Path(__file__).parent
out=root/'dist'
css=(out/'styles.css').read_text()
app=(out/'app.js').read_text()
animations={p.stem:p.read_text() for p in (out/'assets/branding/animations').glob('*.json')}
app=app.replace("fetch(`/assets/branding/animations/${name}-animation.json`).then(r=>{if(!r.ok)throw Error('Animation unavailable');return r.json();})", "Promise.resolve(window.HELLO_ANIMATIONS[`${name}-animation`])")
app=app.replace("const observer=new IntersectionObserver", "const observer=new IntersectionObserver")
app += '\nwindow.helloCleanup=()=>{observer.disconnect();reducedMotion.removeEventListener(\'change\',onMotionChange);$$(\'[data-animation]\').forEach(el=>el._running?.cancel());clearTimeout(toastTimer);};'
# Standalone handoff: all pages and brand images stay inside one offline file.
def inline_assets(html):
 def asset(m):
  p=out/m.group(1).lstrip('/')
  mime={'.svg':'image/svg+xml','.png':'image/png','.ico':'image/x-icon'}[p.suffix]
  return 'src="data:'+mime+';base64,'+base64.b64encode(p.read_bytes()).decode()+'"'
 html=re.sub(r'src="(/assets/[^\"]+)"',asset,html)
 html=re.sub(r'href="/([^"#]*)"',lambda m:'href="#/'+m.group(1)+'"',html)
 html=html.replace('href="/#businesses"','href="#businesses"')
 return html
pages={}
for p in out.rglob('index.html'):
 route='/' if p.parent==out else '/'+str(p.parent.relative_to(out))+'/'
 body=re.search(r'<body id="top">(.*)</body>',p.read_text(),re.S).group(1)
 pages[route]=inline_assets(body)
script='''
window.HELLO_ANIMATIONS=__ANIMATION_DATA__;
const pages=__PAGE_DATA__;
const application=__APP_DATA__;
const mount=()=>{
 window.helloCleanup?.();
 const hash=location.hash;
 let route=hash.startsWith('#/')?hash.slice(1).split('?')[0]:'/';
 if(!route.endsWith('/'))route+='/';
 document.getElementById('site-root').innerHTML=pages[route]||pages['/'];
 new Function(application)();
 window.scrollTo(0,0);
 if(hash==='#businesses')document.getElementById('businesses')?.scrollIntoView();
};
window.addEventListener('hashchange',()=>{if(location.hash.startsWith('#/')||location.hash==='#businesses')mount();});
mount();
'''.replace('__ANIMATION_DATA__',json.dumps({k:json.loads(v) for k,v in animations.items()},separators=(',',':')),1).replace('__PAGE_DATA__',json.dumps(pages,separators=(',',':')),1).replace('__APP_DATA__',json.dumps(app),1)
# Avoid a literal closing script marker inside embedded data.
script=script.replace('</script','<\\/script')
html='<!doctype html><html lang="en-IN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Hello Customer — Website Preview</title><style>'+css+'</style></head><body><div id="site-root"></div><script>'+script+'</script></body></html>'
preview=root.parent/'Hello_Customer_Preview.html';preview.write_text(html)
archive=root.parent/'Hello_Customer_Website.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
 for p in root.rglob('*'):
  if p.is_file() and '.git' not in p.parts and '.DS_Store' not in p.parts and p.suffix not in ('.tar','.gz','.zip'):
   z.write(p,'hello-customer/'+str(p.relative_to(root)))
 z.write(preview,preview.name)
print(f'Created standalone preview ({preview.stat().st_size:,} bytes) and website ZIP ({archive.stat().st_size:,} bytes).')
