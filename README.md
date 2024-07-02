![LinkedIn GPT - Automated job applications tailored to you.](img/github-banner.jpg)

# LinkedIn GPT
Automatically apply to _LinkedIn Easy Apply_ jobs. This bot answers the application questions as well!

This is a fork of a fork of the original _LinkedIn Easy Apply Bot_, but it is a very special fork of a fork, this one relies on LLMs to answer the questions.

> This is for educational purposes only. I am not responsible if your LinkedIn account gets suspended or for anything else.

This bot is written in Python using Selenium and OpenAI.

## Fork Notes
The original bot implementation, couldn't handle open questions, just used keywords and predefined answers. Such couldn't complete a lot of the applications, as any open question or weird selector would make the bot unable to answer. Now that we have LLM, this is an easy problem to solve, just ask the bot to answer the question, and it will do it.

Another great benefit, is that you can provide way more information to the bot, so it can address truthfully the job requirements, and the questions, just as you would do. 

I did try to tidy the code a bit, but I didn't want to spend too much time on it, as I just wanted to get it working, so there is still a lot of work to do there.

Thank you for everyone that contributed to the original bot, and all the forks, made my work way easier.

_by Jorge Frías_

### Future updates
- I will keep updating this fork as I use it for my own "educational research".
- I will add features as I find fun applications, or I require them for my "educational research".

## Setup

### OpenAI API Key
First you need to provide your Open AI API key using environment variable `OPEN_AI_API_KEY`.

> [You can set up the environment variable in your venv](https://stackoverflow.com/a/20918496/8150874)

Certainly! Here are the detailed steps to edit the environment in macOS:

### 1. Create a Virtual Environment
If you haven't already created a virtual environment, do so with the following command:

```bash
python3 -m venv myenv
```

### 2. Activate the Virtual Environment
Activate the virtual environment with the following command:

```bash
source myenv/bin/activate
```

### 3. Edit the Activation Script
To set the `OPEN_AI_API_KEY` environment variable automatically whenever you activate your virtual environment, you need to edit the activation script. Follow these steps:

1. Open the `activate` script in a text editor. You can use any text editor you prefer, like `nano`, `vim`, or `code` (VSCode).

```bash
nano myenv/bin/activate
```

2. Add the following line to the end of the `activate` script:

```bash
export OPEN_AI_API_KEY=your_openai_api_key
```

Replace `your_openai_api_key` with your actual OpenAI API key.

3. Save the file and exit the text editor. In `nano`, you can do this by pressing `CTRL + X`, then `Y` to confirm changes, and `Enter` to save.

### 4. Reactivate the Virtual Environment
To ensure the changes take effect, deactivate and then reactivate your virtual environment:

```bash
deactivate
source myenv/bin/activate
```

### 5. Verify the Environment Variable
Check that the `OPEN_AI_API_KEY` environment variable is set correctly:

```bash
echo $OPEN_AI_API_KEY
```

You should see your API key printed in the terminal.

### Summary
Now, every time you activate your virtual environment with `source myenv/bin/activate`, the `OPEN_AI_API_KEY` environment variable will be set automatically. This ensures your API key is always available in your development environment.
### NOTE
You can ALSO set environment variables globally so they are available in all terminal sessions, not just within a specific virtual environment. 

I recommend to set a [Rate Limit](https://platform.openai.com/account/rate-limits) on your OpenAI account if you plan to leave the bot running for a long time, as it can get expensive quickly. I tried to use the cheapest models possible, but still requires `GPT-3.5-Turbo` to work.

### Your information
Your information is provided with a directory containing the following files:
- `config.yaml`. This file contains the information used to search on LinkedIn and fill in your personal information. Most of this is self-explanatory but if you need explanations please see the end of this `README`.
- `plain_text_resume.md`. Will be used to answer the questions, it's provided in MarkDown format.
- `plain_text_cover_letter.md`. Will be used when the form ask for a cover letter. When the form ask to write a cover letter (not upload it), the bot will adjust the cover letter to the job description.
  - You can use placeholders in your cover letter, a placeholder is defined as `[[placeholder]]`, the LLM will look onto the job description to fill in the placeholders. E.g. `[[company]]` will be replaced by the given company name.
- `personal_data.md`. More information about you, what you want of the job search, work authorization, extended information not covered by the resume, etc. This will be used to answer the questions, and inform other parts of the application. This file doesn't have any structure, will be interpreted by the LLM so fell free to add structure or information as you see fit.
- `job-filters.md`. This file gives you more control over the jobs that the bot applies to. There are two sections: `# Job Title Filters` and `# Job Description Filters` , these must be included on the document, these names are hardcoded on the script __do not modify them__.
- `resume.pdf`. Will be uploaded to LinkedIn when applying. The resume file can have a different name as long as it is a pdf file and the name contains the word `resume`. E.g. `Michael_Scott_Resume.pdf`.
- `cover_letter.pdf`. Will be uploaded to LinkedIn when applying if provided and the job application asks for it. The cover letter file can have a different name as long as it is a pdf file and the name contains the word `cover`. E.g. `Dwight_Schrute_Cover_Letter.pdf`.

  The `# Job Title Filters` section is used to filter the job title, and the `# Job Description Filters` section is used to filter the job description (once the job passes the job title filtering). The information on these sections is used on different steps of the process, you can have different rules on each section, or the same rules on both sections.
  
  Use natural language to explain what you are interested in, and what you are not. The LLM will try to understand what you mean, and will decide to apply or not to the job. 

> An `output` folder will be created, where you will find all generated answers to the questions.

The folder approach enables you to have multiple configurations (based on locations, roles...), and switch between them easily.

**You will find templates for all this files in the `templates` folder.**

### Install required libraries
> You should use a `virtual environment` for this, but it is not required.
```bash
pip3 install -r requirements.txt
```

## Execute
To run the bot, run the following in the command line, providing the path to your personal information directory as only argument.
```bash
python3 main.py path/to/your/personal/information/directory
```

## Config.yaml Explanations
Just fill in your email and password for linkedin.
```yaml
email: suleman361@gmail.com
password: Godisgreat19
```

This prevents your computer from going to sleep so the bot can keep running when you are not using it. Set this to True if you want this disabled.
```yaml
disableAntiLock: False
```

Set this to True if you want to look for remote jobs only.
```yaml
remote: True
```

This is for what level of jobs you want the search to contain. You must choose at least one.
```yaml
experienceLevel:
 internship: False
 entry: True
 associate: True
 mid-senior level: True
 director: False
 executive: False
```

This is for what type of job you are looking for. You must choose at least one.
```yaml
jobTypes:
 full-time: True
 contract: True
 part-time: False
 temporary: False
 internship: False
 other: False
 volunteer: False
```

How far back you want to search. You must choose only one.
```yaml
date:
 all time: True
 month: False
 week: False
 24 hours: False
 ```

A list of positions you want to apply for. You must include at least one.
```yaml
positions:
 #- First position
 #- A second position
 #- A third position
 #- ...
 - iOS Architect
 - Mobile Architect
 - iOS Engineer
 - Flutter developer
 - React Native Developer
 - Mobile Developer
 - Senior Software Engineer 
 ```

A list of locations you are applying to. You must include at least one.
```yaml
locations:
 #- First location
 #- A second location
 #- A third location
 #- ...
 - Remote
 - Dallas, TX
 ```

How far out of the location you want your search to go. You can only input 0, 5, 10, 25, 50, 100 miles.
```yaml
distance: 25
 ```

A list of companies to not apply to.
```yaml
companyBlacklist:
 #- company
 #- company2
 ```

A list of words that will be used to skip over jobs with any of these words in there.
```yaml
titleBlacklist:
 #- word1
 #- word2
 ```

Input your personal info. Include the state/province in the city name to not get the wrong city when choosing from a dropdown.
The phone country code needs to be exact for the one that is on linkedin.
The website is interchangeable for github/portfolio/website.
> This information should also be provided on `personal_data.md`.
```yaml
# ------------ Additional parameters: personal info ---------------
personalInfo:
 First Name: Suleman
 Last Name: Imdad
 Phone Country Code: United States (+1)
 Mobile Phone Number: 4086017007
 Street address: 13836 Bora Bora Way
 City: Marina Del Rey, CA 
 State: California
 Zip: 90292
 Linkedin: https://www.linkedin.com/in/suleman-imdad
 Website: https://www.apportunity.io 
```

# Known issues
- The bot not always replaces correctly the placeholders on the cover letter.
- If any field has problems with the answer, e.g. expected a number and the bot generated a text, the application will not proceed.
- Usually the first screen asking for contact information also ask for a `summary`, gpt doesn't fill this screen, so the application will not proceed.
