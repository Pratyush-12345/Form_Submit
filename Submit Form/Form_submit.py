import requests

# URL of the Google Form endpoint
url = 'https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/formResponse'

# Form data (adjust field names as per your form)
form_data = {
    'entry.2034846182': '',
    'entry.334915649': '',
    'entry.571107327': '',
    'entry.163447158': '',
    'entry.1632541295': '',
    'entry.148364949': '',
    'entry.219783874': '',
    'entry.1848012157_year': '',
    'entry.1848012157_month': '',
    'entry.1848012157_day': '',
}

try:
    # Send POST request with form data
    response = requests.post(url, data=form_data)

    # Check response status
    if response.status_code == 200:
        print('Form submitted successfully!')
    else:
        print(f'Failed to submit form. Status code: {response.status_code}')

except requests.exceptions.RequestException as ex:
    print(f'RequestException: {ex}')
