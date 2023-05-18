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
        program = tracker.get_slot("program")
        if not program:
            dispatcher.utter_message("I'm sorry, I didn't catch the program name. Can you please repeat it?")
            return []

        # Look up career opportunities for the program in a local JSON file, handling misspellings
        with open('/home/tinashe/rasa_projects/BEM-main/actions/career_opportunities.json', 'r') as f:
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
                if score > 0.6 and score > current_score:
                    current_program = p
                    current_score = score
            if current_program is None:
                dispatcher.utter_message(f"I'm sorry, I couldn't find any career opportunities for {program}.")


            else:
                career_opportunities = programs[current_program]
                career_opportunities_str = ', '.join(career_opportunities)
                dispatcher.utter_message(
                    f"Here are some career opportunities for {program}: {career_opportunities_str}")

        return [SlotSet("program", None)]


class ActionInquirePrograms(Action):
    def name(self):
        return "action_inquire_programs"

    def run(self, dispatcher, tracker, domain):
        faculty_program = tracker.get_slot("faculty_program")
        if not faculty_program:
            dispatcher.utter_message(f"I'm sorry, I didn't catch the faculty name {faculty_program} . Can you please "
                                     f"repeat it?")
            return []

        # Look up career opportunities for the program in a local JSON file, handling misspellings
        with open('/home/tinashe/rasa_projects/BEM-main/actions/programs.json', 'r') as f:
            facaulty_programs = None
            current_facaulty = None
            current_score = 0
            facaulty_data = json.load(f)
            # Loop through the dictionary and compare each term with the query
            for p in facaulty_data:
                # Calculate the similarity score between the query and the word
                score = difflib.SequenceMatcher(None, faculty_program, p).ratio()
                # If the score is above the threshold, add the word to the matches list
                print(score)
                if score > 0.6 and score > current_score:
                    current_facaulty = p
                    current_score = score
            if current_facaulty is None:
                dispatcher.utter_message(f"I'm sorry, I couldn't find any career opportunities for {faculty_program}.")


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
                    f"Departments under the  in facaulty of {faculty_program} are : {departments}\n{dept_str}")

        return [SlotSet("faculty_program", None)]


class ActionInquireResearch(Action):
    def name(self):
        return "action_inquire_research"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            "The faculty of business management offers various programs at the undergraduate, graduate, and postgraduate levels. Here are some examples of programs that are offered:1.Bachelor of Business Administration (BBA)\n2.Bachelor of Commerce (BCom)\nMaster of Business Administration (MBA)\n3.Master of Science in Management (MScM)\n Master of Management (MM) Doctor of Business Administration (DBA)\n4.Executive Master of Business Administration (EMBA)\n5.Postgraduate Diploma in Business Administration (PGDBA)\n6.Certificate in Business Management\n7.Diploma in Business Management.In addition to these programs, faculty of business management also offer various specialized programs in areas such as finance, marketing, human resources, entrepreneurship, and international business, among others.")
        return []


class FallbackAction(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("I'm sorry, I didn't understand. Can you please rephrase or try a different query?")

        return []

class ActionInquireContactDetails(Action):
    def name(self):
        return "action_inquire_contact"

    def run(self, dispatcher, tracker, domain):
        faculty = tracker.get_slot("faculty")
        if not faculty:
            dispatcher.utter_message("I'm sorry, I didn't catch the program name. Can you please repeat it?")
            return []

        # Look up career opportunities for the program in a local JSON file, handling misspellings
        with open('/home/tinashe/rasa_projects/BEM-main/actions/contact_details.json', 'r') as f:

            current_faculty = None
            current_score = 0
            contacts = json.load(f)
            # Loop through the dictionary and compare each term with the query
            for p in contacts:
                # Calculate the similarity score between the query and the word
                score = difflib.SequenceMatcher(None, faculty, p).ratio()
                # If the score is above the threshold, add the word to the matches list
                print(score)
                if score > 0.6 and score > current_score:
                    current_faculty = p
                    current_score = score
            if current_faculty is None:
                dispatcher.utter_message(f"I'm sorry, I couldn't find the contact details for  {faculty}.")
            else:
                current_faculty_details = contacts[current_faculty]
                faculty_details = '\n'.join(current_faculty_details)
                dispatcher.utter_message(
                    f"Contact details for faculty of {faculty}: {faculty_details}")

        return [SlotSet("faculty", None)]


class ActionInquirePassion(Action):
    def name(self):
        return "action_inquire_passion"

    def run(self, dispatcher, tracker, domain):
        passion = tracker.get_slot("passion")
        if not passion:
            dispatcher.utter_message("I'm sorry, I didn't catch the program name. Can you please repeat it?")
            return []

        # Look up career opportunities for the program in a local JSON file, handling misspellings
        with open('/home/tinashe/rasa_projects/BEM-main/actions/passion.json', 'r') as f:

            current_passion = None
            current_score = 0
            passions = json.load(f)
            # Loop through the dictionary and compare each term with the query
            for p in passions:
                # Calculate the similarity score between the query and the word
                score = difflib.SequenceMatcher(None, passion, p).ratio()
                # If the score is above the threshold, add the word to the matches list
                print(score)
                if score >= 0.5 and score > current_score:
                    current_passion = p
                    current_score = score
            if current_passion is None:
                dispatcher.utter_message(f"I'm sorry, I couldn't find the contact details for  {passion}.")
            else:
                current_passion_programs = passions[current_passion]['programs']
                print()
                passion_description = passions[current_passion]['description']
                passion_details = '\n'.join(current_passion_programs)

                dispatcher.utter_message(
                    f"According to your interest {passion_details} may be better suited for you\n {passion_description}")

        return [SlotSet("passion", None)]
