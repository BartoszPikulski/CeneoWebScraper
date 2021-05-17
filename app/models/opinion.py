from app.utils import extract_element

class Opinion:
    
    selectors = {
            "opinion_id": ["data-entry-id"],
            "author": ["span.user-post__author-name"],
            "recommendation": ["span.user-post__author-recomendation > em"],
            "stars": ["span.user-post__score-count"],
            "content": ["div.user-post__text"],
            "cons": ["div.review-feature__col:has(> div[class*='positives']) > div.review-feature__item",1],
            "pros": ["div.review-feature__col:has(> div[class*=\"negatives\"]) > div.review-feature__item",1],
            "purchased": ["div.review-pz"],
            "submit_date": ["span.user-post__published > time:nth-of-type(1)", "datetime"],
            "purchase_date": ["span.user-post__published > time:nth-of-type(2)", "datetime"],
            "useful" : ["span[id^=\"votes-yes\"]"],
            "useless" : ["span[id^=\"votes-no\"]"]
    }

    def __init__(self, opinion_id = None):
        self.opinion_id = opinion_id

    def extract_opinion(self, opinion):
        for key, args in self.selectors.items():
            setattr(self, key, extract_element(opinion, *args))
        self.opinion_id = opinion["data-entry-id"]


        opinion_elements["recommendation"] = True if opinion_elements[
                "recommendation"] == "Polecam" else False if opinion_elements["recommendation"] == "Nie polecam" else None
        opinion_elements["stars"] = float(opinion_elements["stars"].split("/")[0].replace(",", "."))
        opinion_elements["purchased"] = bool(opinion_elements["purchased"])
        opinion_elements["useful"] = int(opinion_elements["useful"])
        opinion_elements["useless"] = int(opinion_elements["useless"])
 