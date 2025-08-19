from .models import CompanyDetail, SocialMedia

import json

def get_company_details(request):
    try:
        company = CompanyDetail.objects.all().last()
        social = SocialMedia.objects.filter(enable=True)
    except Exception as e:
        print('Exception in context_processor of main: ', e)

    return {
        'company': company,
        'social': social
    }

def display_navbar(request):
    try:
        file_obj = open('nav_json.json')
        json_obj = json.load(file_obj)
        
        navbars = json_obj['navbars']

        # Copy navbar list to footer list to extend footer extra navs
        footar_navbars = navbars[:]

        # Adding footer navbars
        for nav in json_obj['footar-navbars']:
            footar_navbars.append(nav)

    except Exception as e:
        print('Exception in display_navbar page context : ', e)

    return {
        'navbars': navbars,
        'footar_navbars': footar_navbars
    }