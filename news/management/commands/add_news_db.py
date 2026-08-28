import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from news.models import News


class Command(BaseCommand):
    help = 'Load 5 news from Fake.csv into the News model'

    def handle(self, *args, **kwargs):
        csv_file_path = 'news/management/commands/Fake.csv'
        created_count = 0

        try:
            with open(csv_file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                cont = 0

                for row in reader:
                    if cont == 5:
                        break

                    date_str = row['date'].strip()
                    formatted_date = datetime.strptime(date_str, '%B %d, %Y').date()

                    _, created = News.objects.get_or_create(
                        headline=row['title'],
                        defaults={
                            'body': row['text'],
                            'date': formatted_date,
                        }
                    )

                    if created:
                        created_count += 1
                    cont += 1

            self.stdout.write(
                self.style.SUCCESS(f'Import completed. Created: {created_count}')
            )

        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f'File not found: {csv_file_path}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Unexpected error: {e}')
            )