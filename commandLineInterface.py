import argparse
from pathlib import Path
from main import validate_data_folder, validate_yaml, file_paths_to_dict, build_parameters, args_datafolder
from gpt import GPTAnswerer


class CommandLineInterface:
    def __init__(self, data_folder: Path):
        # I don't like dicts to pass fields known at "compile" time, but reuse the LinkedIn bot code is easier
        parameters = build_parameters(data_folder)

        # Data to fill in the application using GPT
        # - Plain text resume
        plain_text_resume_path = parameters['uploads']['plainTextResume']
        file = open(plain_text_resume_path, "r")  # Read the file
        plain_text_resume: str = file.read()
        # - Plain text personal data
        plain_text_personal_data_path = parameters['uploads']['plainTextPersonalData']
        file = open(plain_text_personal_data_path, "r")  # Read the file
        plain_text_personal_data: str = file.read()
        # - Plain text cover letter
        plain_text_cover_letter_path = parameters['uploads']['plainTextCoverLetter']
        file = open(plain_text_cover_letter_path, "r")  # Read the file
        plain_text_cover_letter: str = file.read()
        # - Job filters
        job_filters_path = parameters['uploads']['jobFilters']
        file = open(job_filters_path, "r")  # Read the file
        job_filters: str = file.read()

        # - Build the GPT answerer using the plain text data
        self.gpt_answerer = GPTAnswerer(plain_text_resume, plain_text_personal_data, plain_text_cover_letter, job_filters)

    def provide_new_job_description(self, job_description: str):
        # I think the job description summarization process is unnecessary overhead
        self.gpt_answerer.job_description_summary = job_description

    def answer(self, question: str) -> str:
        return self.gpt_answerer.answer_question_textual_wide_range(question)

    def command_line_loop(self):
        commands_with_description = {
            'help': 'Print this help',
            'exit': 'Exit the program',
            'answer': 'Ask a question to the bot',
            'job': 'Provide a new job description to the bot',
            'cover': 'Provide a new cover letter to the bot'
        }

        while True:
            command = input("Enter a command (help for help): ")
            if command == 'help':
                for command in commands_with_description:
                    print(f"{command}: {commands_with_description[command]}")
            elif command == 'exit':
                break
            elif command == 'answer':
                question = input("Enter a question: ")
                answer = self.answer(question)
                print(f"{answer}")
            elif command == 'job':
                job_description = input("Enter a job description: ")
                # Multiline input, stop on five consecutive empty lines
                empty_lines = 0
                while True:
                    line = input()
                    if line == '':
                        empty_lines += 1
                        if empty_lines == 5:
                            break
                    else:
                        empty_lines = 0
                    job_description += line + '\n'

                self.provide_new_job_description(job_description)
                print("Job description provided")
            elif command == 'cover':
                self.gpt_answerer.
            else:
                print(f"Unknown command {command}")


if __name__ == "__main__":
    # Parse the command line arguments to extract the data folder
    data_folder = args_datafolder()
    # Create the command line interface
    command_line_interface = CommandLineInterface(data_folder)
    # Start the command line interface loop
    command_line_interface.command_line_loop()
