import requests
from datetime import date, time, datetime

# Documentation: https://developers.google.com/speed/docs/insights/v5/get-started

# Populate 'pagespeed.txt' file with URLs to query against API.
with open('pagespeed.txt') as pagespeedurls:
    download_dir = 'pagespeed-results.csv'
    file = open(download_dir, 'a')
    content = pagespeedurls.readlines()
    content = [line.rstrip('\n') for line in content]

    # This is the google pagespeed api url structure, using for loop to insert each url in .txt file
    for line in content:
        # If no "strategy" parameter is included, the query by default returns desktop data.
        apiKey = 'AIzaSyA54CB4HdlHF8yTmgVnHEyHr696Ufyqozs'
        x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={line}&key={apiKey}&strategy=mobile'
        print(f'Requesting {x}...')
        r = requests.get(x)
        final = r.json()
        
        try:
            urlid = final['id']
            split = urlid.split('?') # This splits the absolute url from the api key parameter
            urlid = split[0] # This reassigns urlid to the absolute url
            ID = f'URL ~ {urlid}'
            ID2 = str(urlid)
            today = date.today()
            now = datetime.now()
            current_time = time(now.hour, now.minute, now.second)
            DATE= datetime.combine(today, current_time)
            urlpsi = final['lighthouseResult']['categories']['performance']['score']
            PSI = f'PageSpeed Score ~ {str(urlpsi * 100)}'
            PSI2 = str(urlpsi * 100)
            urlfcp = final['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
            FCP = f'First Contentful Paint ~ {str(urlfcp)}'
            FCP2 = str(urlfcp)
            urltti = final['lighthouseResult']['audits']['interactive']['displayValue']
            TTI = f'Time to Interactive ~ {str(urltti)}'
            TTI2 = str(urltti)
            urllcp = final['lighthouseResult']['audits']['largest-contentful-paint']['displayValue']
            LCP = f'Largest Contentful Paint ~ {str(urllcp)}'
            LCP2 = str(urllcp)
            urlsi = final['lighthouseResult']['audits']['speed-index']['displayValue']
            SI = f'Speed Index ~ {str(urlsi)}'
            SI2 = str(urlsi)
            urlfmp = final['lighthouseResult']['audits']['first-meaningful-paint']['displayValue']
            FMP = f'First Meaningful Paint ~ {str(urlfmp)}'
            FMP2 = str(urlfmp)
            urlfci = final['lighthouseResult']['audits']['first-cpu-idle']['displayValue']
            FCI = f'First CPI Idle ~ {str(urlfci)}'
            FCI2 = str(urlfci)
            urleil = final['lighthouseResult']['audits']['max-potential-fid']['displayValue']
            EIL = f'Estimated Input Latency ~ {str(urleil)}'
            EIL2 = str(urleil)
            urltbt = final['lighthouseResult']['audits']['total-blocking-time']['displayValue']
            TBT = f'Total Blocking Time ~ {str(urltbt)}'
            TBT2 = str(urltbt)
            urlcls = final['lighthouseResult']['audits']['cumulative-layout-shift']['displayValue']
            CLS = f'Cumulative Layout Shift ~ {str(urlcls)}'
            CLS2 = str(urlcls)
        except KeyError:
            print(f'<KeyError> One or more keys not found {line}.')
        
        try:
            row = f'{DATE},{ID2},{PSI2},{FCP2},{TTI2},{LCP2},{SI2},{FMP2},{FCI2},{EIL2},{TBT2},{CLS2}\n'
            file.write(row)            
        except NameError:
            print(f'<NameError> Failing because of KeyError {line}.')
            file.write(f'<KeyError> & <NameError> Failing because of nonexistant Key ~ {line}.' + '\n')
        
        try:
            print(DATE)
            print(ID)
            print(PSI) 
            print(FCP)
            print(TTI)
            print(LCP)
            print(SI)
            print(FMP)
            print(FCI)
            print(EIL)
            print(TBT)
            print(CLS)
        except NameError:
            print(f'<NameError> Failing because of KeyError {line}.')

    file.close()
