import random

from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation


def get_schoolkid(fullname):
    try:
        return Schoolkid.objects.get(full_name__contains=fullname)
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников с таким ФИО")
    except Schoolkid.DoesNotExist:
        print("Не найден ученик с таким ФИО")


def fix_bad_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def delete_chastisements(schoolkid):
    childs_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    childs_chastisements.delete()


def create_commendation(schoolkid, subject):
    commendations = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!'
        ]
    try:
        lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject__title__contains=subject).order_by('date').last()
        Commendation.objects.create(text=random.choice(commendations), created=lesson.date, schoolkid=schoolkid, subject=lesson.subject, teacher=lesson.teacher)
    except:
        print("Указано неправильное или несуществующее название предмета")