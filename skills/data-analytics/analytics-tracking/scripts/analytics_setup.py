#!/usr/bin/env python3
"""
Analytics Setup Generator
Generates implementation code for various analytics providers
"""

import argparse
import json
import os
from pathlib import Path

def generate_google_analytics(website_url):
    """Generate Google Analytics 4 implementation"""
    return f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', 'G-XXXXXXXXXX');
  gtag('config', 'G-XXXXXXXXXX', {{'page_title': document.title, 'page_location': window.location.href}});
</script>

<!-- Event Tracking Example -->
<script>
function trackButtonClick(buttonId, eventName) {{
  gtag('event', eventName, {{
    'button_id': buttonId,
    'page_title': document.title,
    'page_location': window.location.href
  }});
}}
</script>"""

def generate_google_tag_manager(website_url):
    """Generate Google Tag Manager implementation"""
    return f"""<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','GTM-XXXXXX');</script>
<!-- End Google Tag Manager -->

<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

def generate_amplitude(website_url):
    """Generate Amplitude implementation"""
    return f"""<!-- Amplitude Analytics -->
<script type="text/javascript">
(function(e,t){{var n=e.amplitude||{{}};var r=t.createElement("script");r.type="text/javascript";
r.async=true;r.src="https://cdn.amplitude.com/libs/amplitude-8.20.0-min.gz.js";
r.onload=function(){{if(e.amplitude.runQueuedFunctions){{e.amplitude.runQueuedFunctions();}}}};
var s=t.getElementsByTagName("script")[0];s.parentNode.insertBefore(r,s);
function f(e,t){{e.prototype[t]=function(){{this._q.push([t].concat(Array.prototype.slice.call(arguments,0)));
return this;}};}}var o=function(){{this._q=[];return this;}};var a=["add","append","clearAll","prepend",
"set","setOnce","unset","preInsert","postInsert","remove","getUserProperties"];for(var u=0;u<a.length;u++){{f(o,a[u]);}}
n.Identify=o;var c=function(){{this._q=[];return this;}};var l=["setProductId","setQuantity","setPrice",
"setRevenueType","setEventProperties"];for(var u=0;u<l.length;u++){{f(c,l[u]);}}n.Revenue=c;
var p=function(){{this._q=[];return this;}};var d=["init","logEvent","logRevenue","setUserId","setUserProperties",
"setOptOut","setVersionName","setDomain","setDeviceId","enableTracking","setGlobalUserProperties",
"identify","clearUserProperties","setGroup","logRevenueV2","regenerateDeviceId","groupIdentify","onInit",
"logEventWithTimestamp","logEventWithGroups","setSessionId","setTransport","setServerZone",
"setEventUploadPeriodMillis","setEventUploadThreshold"];for(var v=0;v<d.length;v++){{f(p,d[v]);}}n.Sdk=p;
n.createInstance=function(e){{n._q.push(["createInstance",e]);return n._q[n._q.length-1];}};
e.amplitude=n;}})(window,document);

amplitude.init("YOUR_API_KEY_HERE", null, {{defaultTracking: {{sessions: true, pageViews: true, formInteractions: true, fileDownloads: true}}}});
</script>"""

def main():
    parser = argparse.ArgumentParser(description='Generate analytics implementation code')
    parser.add_argument('--provider', required=True, help='Analytics provider (google-analytics, google-tag-manager, amplitude, mixpanel)')
    parser.add_argument('--url', required=True, help='Website URL')
    parser.add_argument('--output', help='Output file path')
    
    args = parser.parse_args()
    
    providers = {
        'google-analytics': generate_google_analytics,
        'google-tag-manager': generate_google_tag_manager,
        'amplitude': generate_amplitude,
        'mixpanel': lambda url: '# Mixpanel implementation template\n# See: https://developer.mixpanel.com/docs/javascript-full-api-reference',
        'segment': lambda url: '# Segment implementation template\n# See: https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/',
        'matomo': lambda url: '# Matomo implementation template\n# See: https://developer.matomo.org/guides/tracking-javascript-guide',
        'plausible': lambda url: '# Plausible Analytics implementation\n<script defer data-domain="yourdomain.com" src="https://plausible.io/js/script.js"></script>'
    }
    
    if args.provider not in providers:
        print(f"Unknown provider: {args.provider}")
        print(f"Available providers: {', '.join(providers.keys())}")
        return 1
    
    implementation = providers[args.provider](args.url)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(implementation)
        print(f"Implementation saved to: {args.output}")
    else:
        print(implementation)
    
    return 0

if __name__ == '__main__':
    exit(main())
