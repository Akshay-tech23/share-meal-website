"""Generate deployment metadata from the single site.config.json source."""
from pathlib import Path
import json, re, html
from urllib.parse import urlsplit
p=Path(__file__).resolve().parents[1]
c=json.loads((p/'site.config.json').read_text())
u=c['siteUrl'].rstrip('/')+'/'
if urlsplit(u).scheme!='https' or not urlsplit(u).netloc:
    raise SystemExit('Set siteUrl to your real HTTPS website URL in site.config.json first.')
(p/'assets/js/config.js').write_text('window.SHARE_MEAL_CONFIG = '+json.dumps(c,indent=2)+';\n')
for name in ['index.html','privacy.html','404.html']:
    f=p/name;s=f.read_text()
    s=re.sub(r'<link rel="canonical"[^>]*>|<meta property="og:url"[^>]*>','',s)
    page=u+('' if name=='index.html' else name)
    s=s.replace('</head>',f'<link rel="canonical" href="{html.escape(page,quote=True)}"><meta property="og:url" content="{html.escape(page,quote=True)}"></head>')
    s=re.sub(r'<meta property="og:image"[^>]*>',f'<meta property="og:image" content="{html.escape(u,quote=True)}assets/images/social.png">',s)
    if name=='404.html':
        # Absolute site paths are necessary when GitHub serves 404 for a nested URL.
        for prefix in ['assets/','favicon.svg','index.html','privacy.html']:
            s=s.replace('="'+prefix,'="'+u+prefix)
        s=s.replace('</head>','<meta name="robots" content="noindex"></head>') if 'content="noindex"' not in s else s
    f.write_text(s)
(p/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+u+'sitemap.xml\n')
(p/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+html.escape(u+x)+'</loc></url>' for x in ['','privacy.html'])+'</urlset>\n')
print('Configured metadata for '+u)
