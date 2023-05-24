# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from Levenshtein import distance
import difflib


class ActionInquireCareerOpportunities(Action):
    def name(self):
        return "action_inquire_career_opportunities"

    def run(self, dispatcher, tracker, domain):
        program = tracker.get_slot("faculty_program")
        if not program:
            dispatcher.utter_message("I'm sorry, I didn't catch the program name. Can you please repeat it?")
            return []

        # Look up career opportunities for the program in a local JSON file, handling misspellings
        with open('actions/career_opportunities.json', 'r') as f:
            career_opportunities = None
            current_program = None
            current_score = 0
            programs = json.load(f)
            # Loop through the dictionary and compare each term with the query
            for p in programs:
                # Calculate the similarity score between the query and the word
                score = difflib.SequenceMatcher(None, program, p).ratio()
                # If the score is above the threshold, add the word to the matches list
                print(score)
                if score > 0.5 and score > current_score:
                    current_program = p
                    current_score = score
            if current_program is None:
                dispatcher.utter_message(f"I'm sorry, I couldn't find any career opportunities for {program}.")
                return [SlotSet("faculty_program", None)]


            else:
                career_opportunities = programs[current_program]
                career_opportunities_str = ', '.join(career_opportunities)
                dispatcher.utter_message(
                    f"Here are some career opportunities for {program}: {career_opportunities_str}")

        return [SlotSet("faculty_program", None)]


class ActionInquirePrograms(Action):
    def name(self):
        return "action_inquire_programs"

    def run(self, dispatcher, tracker, domain):
        faculty_program = tracker.get_slot("faculty_program")
        print(f"The faculty {faculty_program}")
        if not faculty_program:
            dispatcher.utter_message(f"I'm afraid I don't know how to handle that. Could you please try something else?")
            return []

        # Look up career opportunities for the program in a local JSON file, handling misspellings
        with open('actions/programs.json', 'r') as f:
            facaulty_programs = None
            current_facaulty = None
            current_score = 0
            facaulty_data = json.load(f)
            # Loop through the dictionary and compare each term with the query
            for p in facaulty_data:
                # Calculate the similarity score between the query and the word
                score = difflib.SequenceMatcher(None, faculty_program, p).ratio()
                # If the score is above the threshold, add the word to the matches list
                print(f'{score} ,{p} ')
                if score > 0.3 and score > current_score:
                    current_facaulty = p
                    current_score = score
            print(f"Current Faculty {current_facaulty}")
                    
            if current_facaulty is None:
                dispatcher.utter_message(f"No programs for {faculty_program}")
                return [SlotSet("faculty_program", None)]


            else:

                faculty_depts = facaulty_data[current_facaulty]

                depts = list(faculty_depts['departments'])
                departments = ', '.join(depts)
                dept_str = ''

                for dept in depts:
                    dept_data = faculty_depts['departments'][dept]
                    under_grad = '\n'.join(dept_data['undergraduate'])
                    post_grad = '\n'.join(dept_data['postgraduate'])
                    dept_str = dept_str + f'\nPrograms under department of *{dept}*\n*Undergraduate Programs*\n{under_grad}\n*Postgraduate programs*\n{post_grad} '
                dispatcher.utter_message(
                    f"Departments under the  in facaulty of {current_facaulty} are : {departments}\n{dept_str}")

        return [SlotSet("faculty_program", None)]




class FallbackAction(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("I'm sorry, I didn't understand. Can you please rephrase or try a different query?")

        return []

class ActionInquireFees(Action):
    def name(self):
        return "action_inquire_fees"

    def run(self, dispatcher, tracker, domain):
        faculty = tracker.get_slot("faculty_program")
        if not faculty:
            dispatcher.utter_message("I'm sorry, I didn't catch the program name. Can you please rephrase it?")
            return []

        # Look up career opportunities for the program in a local JSON file, handling misspellings
        with open('actions/fees.json', 'r') as f:

            current_faculty = None
            current_score = 0
            fees_data = json.load(f)
            # Loop through the dictionary and compare each term with the query
            for p in fees_data:
                # Calculate the similarity score between the query and the word
                score = difflib.SequenceMatcher(None, faculty, p).ratio()
                # If the score is above the threshold, add the word to the matches list
                print(score)
                if score > 0.5 and score > current_score:
                    current_faculty = p
                    current_score = score
            if current_faculty is None:
                dispatcher.utter_message(f"No fees structure for  {faculty}. where found!")
                return [SlotSet("faculty_program", None)]
            else:
                current_faculty_fees = fees_data[current_faculty]
                faculty_fees_details = current_faculty_fees
                dispatcher.utter_message(
                    f"All {current_faculty} students pays {faculty_fees_details} tution fee per semester. However the fees is subject to changes.")

        return [SlotSet("faculty_program", None)]


class ActionInquirePassion(Action):
    def name(self):
        return "action_inquire_passion"

    def run(self, dispatcher, tracker, domain):
        passion = tracker.get_slot("faculty_program")
        if not passion:
            dispatcher.utter_message("I'm sorry, I didn't understand your passion. Could you please rephrase?")
            return []

        # Look up career opportunities for the program in a local JSON file, handling misspellings
        with open('actions/passion.json', 'r') as f:

            current_passion = None
            current_score = 0
            passions = json.load(f)
            # Loop through the dictionary and compare each term with the query
            for p in passions:
                # Calculate the similarity score between the query and the word
                score = difflib.SequenceMatcher(None, passion, p).ratio()
                # If the score is above the threshold, add the word to the matches list
                print(score)
                if score >= 0.3 and score > current_score:
                    current_passion = p
                    current_score = score
            if current_passion is None:
                dispatcher.utter_message(f"I couldn't find a program that matches your passion.")
                return [SlotSet("faculty_program", None)]
            else:
                current_passion_programs = passions[current_passion]['programs']
                print()
                passion_description = passions[current_passion]['description']
                passion_details = '\n'.join(current_passion_programs)

                dispatcher.utter_message(
                    f"According to your interest {passion_details} may be better suited for you\n {passion_description}")

        return [SlotSet("faculty_program", None)]
    
class ActionRetrieveRequirements(Action):
    def name(self):
        return "action_inquire_requirements"
    def run(self, dispatcher, tracker, domain):
        program = tracker.get_slot("faculty_program")
        if not program:
            dispatcher.utter_message("You did'nt specify the program. Can you repeat the query with the program specified")
            return []

        # Look up career opportunities for the program in a local JSON file, handling misspellings
        with open('actions/requirements.json', 'r') as f:

            current_faculty = None
            current_score = 0
            requirements_data = json.load(f)
            # Loop through the dictionary and compare each term with the query
            for p in requirements_data:
                # Calculate the similarity score between the query and the word
                score = difflib.SequenceMatcher(None, program, p).ratio()
                # If the score is above the threshold, add the word to the matches list
                print(score)
                if score > 0.5 and score > current_score:
                    current_faculty = p
                    current_score = score
            if current_faculty is None:
                dispatcher.utter_message(f"No fees structure for  {program}. where found!")
                return [SlotSet("faculty_program", None)]
            else:
                current_program_requirements = requirements_data[current_faculty]
                program_details = '\n'.join(current_program_requirements['requirements'])
                
                dispatcher.utter_message(
                    f"For you to get enrolled in {current_faculty}, you must meet the following requirements.\n{program_details}.\nIn addition to the above ,  ️⃣You must have passed at least 5🖐 subjects, including English language 📚 at ‘O’ level and at least 2✌ ‘A’ Level passes or equivalent. ✅  2️⃣You must pay a non-refundable application fee of US$2️⃣0️⃣ for Zimbabweans and US$5️⃣0️⃣ for International Students at any CBZ Branch nation wide 💳 3️⃣You must fill out an application form 📝 and submit it to the Senior Assistant Registrar (Admissions) at the University of Zimbabwe. 🏫 4️⃣You must also make an online application 💻 at UZ campus on www.emhare.uz.ac.zw. 🌐")

        return [SlotSet("faculty_program", None)]
