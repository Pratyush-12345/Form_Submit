# Google Form Automation

This project demonstrates how to automate the submission of a Google Form using Python's `requests` library. Additionally, it includes a JavaScript snippet to find the necessary input tags in the console.

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library

### Installation

1. Clone the repository:

    - `git clone https://github.com/your-username/Form_Submit.git`
    - `cd Form_Submit`

2. Install the `requests` library:

    - `pip install requests`

### Usage

1. Identify the form endpoint URL:

    - Open the Google Form in your browser.
    - Inspect the form using developer tools (F12 or right-click > Inspect).
    - Look for the form's `action` attribute which contains the endpoint URL.

2. Identify the input field names:

    - In the developer tools console, run the following JavaScript snippet to list all input tags and their names:

      ```javascript
      document.querySelectorAll('input').forEach(input => console.log(input.name));
      ```

3. Update the Python script with the form endpoint URL and input field names:

    - Replace the `url` variable with the form's endpoint URL.
    - Update the `form_data` dictionary with the appropriate field names and values.

4. Run the Python script to submit the form:

    - `python submit_form.py`

### Troubleshooting

- Ensure that all required fields in the form are included in the `form_data` dictionary.
- Double-check the field names and endpoint URL.
- Verify your internet connection.

### Contributing

Feel free to submit issues or pull requests for any improvements or bug fixes.

