# import_csv.py

import csv
from  base.models import Poems

with open('all_poems.csv', 'rt',encoding='utf-8') as f:
    data_reader = csv.reader(f, delimiter=',', quotechar='"')
    next(data_reader)
    
    for row in data_reader:
        poem = Poems()
        poem.poem_id = row[0]
        poem.poem_link = row[1]
        poem.poem_style = row[2]
        poem.poem_text = row[3]
        poem.poem_title = row[4]
        poem.poet_cat = row[5]
        poem.poet_id = row[6]
        poem.poet_link = row[7]
        poem.poet_name = row[8]
        poem.save()


# import pandas as pd
# from django.core.management.base import BaseCommand
# from base import Poems
# # from sqlalchemy import create_engine
# from django.conf import settings

# class Command(BaseCommand):
#   help = "A command to add data from an Excel file to the database"

#   def handle(self, *args, **options):

#     excel_file = 'all_poems.csv'
#     df = pd.read_csv(excel_file)
#     print(df)
#     user = settings.DATABASES['default']['USER']
#     password = settings.DATABASES['default']['PASSWORD']
#     database_name = settings.DATABASES['default']['NAME']

#     # engine = create_engine('sqlite:///db.sqlite3')
#     database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format( user=user,password=password,database_name=database_name,)

#     engine = create_engine(database_url, echo=False)

#     df.to_sql(Poems._meta.db_table, if_exists='replace', con=engine, index=False)
# # import pandas as pd
# # from django.contrib.auth.models import User
# # from base import Poems, poets

# # # Read CSV file into a DataFrame
# # csv_file_path = r"C:\Users\Admin\Desktop\CS471-env\CS471_project\static\all_poems.csv"
# # df = pd.read_csv(csv_file_path)

# # for index, row in df.iterrows():
# #     poet = poets(
# #     poet_id = row['poet_id'],
# #     poet_cat = row['poet_cat'],
# #     poet_link = row['poet_link'],
# #     poet_name = row['poet_name'],
# #     )

# #     poet.save()

# #     poem = Poems(
# #         poem_id = row['poem_id'],
# #         poem_link = row['poem_link'],
# #         poem_style = row['poem_style'],
# #         poem_text = row['poem_text'],
# #         poem_title = row['poem_title'],
# #         poet_id = row['poet_id'],
# #         poet_cat = row['poet_cat'],
# #         poet_link = row['poet_link'],
# #         poet_name = row['poet_name'],
# #     )

# #     poem.save()

# # print("CSV data has been loaded into the Django database.")