import uuid
from random import randrange, choice
import csv
from enum import Enum
from datetime import datetime, timedelta, date
from typing import List, Tuple

class TestGroup(Enum):
    control = 'control'
    test = 'test'
    unparticipation = 'unparticipation'

class Regions(Enum):
    Moscow = 'Moscow'
    Saint_Petersburg = 'Saint Petersburg'
    Novosibirsk = 'Novosibirsk'
    Yekaterinburg = 'Yekaterinburg'
    Kazan = 'Kazan'
    Chelyabinsk = 'Chelyabinsk'
    Omsk = 'Omsk'
    Samara = 'Samara'
    region = 'region'

class MarketingGroup(Enum):
    social_media = 'social_media'
    target = 'target'
    email_marketing = 'email_maketing'

class ProductReview(Enum):
    video = 'video'
    photo = 'photo'
    video_and_photo = 'video_and_photo'
    text = 'text'
    no_reviews = 'no_reviews'

def random_date(start: datetime, end: datetime):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def generate_records(test_group: TestGroup, time_to_order_range: Tuple[int], records_count: int) -> List[dict]:
    first_date, last_date = date(2022, 3, 1), date(2022, 3, 21) 
    result = []
    for i in range(records_count):
        first_visit_at = random_date(first_date, last_date)
        time_to_order = randrange(*time_to_order_range)
        order_completed_at = first_visit_at + timedelta(hours=time_to_order)
        record = dict(userid=uuid.uuid4().hex,
                      test_group=test_group.value,
                      time_to_order=time_to_order,
                      first_visit_at=first_visit_at.isoformat(),
                      order_completed_at=order_completed_at.isoformat(),
                      region=choice([i.value for i in Regions]),
                      marketing_group=choice([i.value for i in MarketingGroup]),
                      product_review=choice([i.value for i in ProductReview]),
                      successful_orders=randrange(1, 20),
                      average_receipt_rub=randrange(1337, 84999),
                      read_pushes=randrange(0, 33),
                      )
        result.append(record)
    return result
    

with open('names.csv', 'w', newline='') as csvfile:
    headers = ['userid', 'test_group', 'first_visit_at',
               'order_completed_at', 'time_to_order', 'region',
               'marketing_group', 'product_review', 'successful_orders',
               'average_receipt_rub', 'read_pushes']
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    
    test_group = generate_records(TestGroup.test, (2, 72), 530)
    control_group = generate_records(TestGroup.control, (4, 80), 530)
    unparticipation_group = generate_records(TestGroup.unparticipation, (96, 144), 1000)
    
    for i in control_group:
        writer.writerow(i)
    for i in test_group:
        writer.writerow(i)
    for i in unparticipation_group:
        writer.writerow(i)
