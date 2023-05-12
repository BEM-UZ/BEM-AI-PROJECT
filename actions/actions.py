# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from Levenshtein import distance

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

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
            programs = json.load(f)
            for p in programs:
                if p.lower() == program.lower():
                    career_opportunities = programs[p]
                    break
                elif distance(p.lower(), program.lower()) <= 2:
                    career_opportunities = programs[p]

        if not career_opportunities:
            dispatcher.utter_message(f"I'm sorry, I couldn't find any career opportunities for {program}.")
        else:
            career_opportunities_str = ', '.join(career_opportunities)
            dispatcher.utter_message(f"Here are some career opportunities for {program}: {career_opportunities_str}")

        return []
    
class ActionInquireCareerPrograms(Action):
    def name(self):
        return "action_inquire_career_programs"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("A faculty of business management typically offers various programs at the undergraduate, graduate, and postgraduate levels. Here are some examples of programs that may be offered:Bachelor of Business Administration (BBA)Bachelor of Commerce (BCom) Master of Business Administration (MBA) Master of Science in Management (MScM) Master of Management (MM) Doctor of Business Administration (DBA) Executive Master of Business Administration (EMBA) Postgraduate Diploma in Business Administration (PGDBA) Certificate in Business Management Diploma in Business Management In addition to these programs, faculties of business management may also offer various specialized programs in areas such as finance, marketing, human resources, entrepreneurship, and international business, among others. The programs offered by a specific faculty of business management may vary depending on the institution and its focus.")
        return []
        # program = tracker.get_slot("programs")
        # if not program:
        #     dispatcher.utter_message("I'm sorry, I didn't catch the program name. Can you please repeat it?")
        #     return []

        # # Look up career opportunities for the program in a local JSON file, handling misspellings
        # with open('/home/tinashe/rasa_projects/BEM-main/actions/career_opportunities.json', 'r') as f:
        #     career_opportunities = None
        #     programs = json.load(f)
        #     for p in programs:
        #         if p.lower() == program.lower():
        #             career_opportunities = programs[p]
        #             break
        #         elif distance(p.lower(), program.lower()) <= 2:
        #             career_opportunities = programs[p]

        # if not career_opportunities:
        #     dispatcher.utter_message(f"I'm sorry, I couldn't find any career opportunities for {program}.")
        # else:
        #     career_opportunities_str = ', '.join(career_opportunities)
        #     dispatcher.utter_message(f"Here are some career opportunities for {program}: {career_opportunities_str}")

        # return []

class ActionInquireResearch(Action):
    def name(self):
        return "action_inquire_research"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("The faculty of business management offers various programs at the undergraduate, graduate, and postgraduate levels. Here are some examples of programs that are offered:1.Bachelor of Business Administration (BBA)\n2.Bachelor of Commerce (BCom)\nMaster of Business Administration (MBA)\n3.Master of Science in Management (MScM)\n Master of Management (MM) Doctor of Business Administration (DBA)\n4.Executive Master of Business Administration (EMBA)\n5.Postgraduate Diploma in Business Administration (PGDBA)\n6.Certificate in Business Management\n7.Diploma in Business Management.In addition to these programs, faculty of business management also offer various specialized programs in areas such as finance, marketing, human resources, entrepreneurship, and international business, among others.")
        return []
    
class FallbackAction(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("I'm sorry, I didn't understand. Can you please rephrase or try a different query?")
        
        return []