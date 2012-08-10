# -*- coding: utf-8 -*-

import os
import yaml
from nbg.models import Course, Lesson, Semester
from django.core.management.base import BaseCommand, CommandError

def list_to_comma_separated(l):
    return ",".join(map(str, l))

class Command(BaseCommand):
    args = '<semester_id, directory>'
    help = 'Import courses from YAML files'

    def handle(self, *args, **options):
        try:
            semester_id = int(args[0])
            dir = args[1]
        except IndexError, ValueError:
            raise CommandError('Invalid syntax.')

        try:
            files = os.listdir(dir)
        except OSError:
            raise CommandError('Directory not exist.')
        files = [f for f in files if
          os.path.isfile(os.path.join(dir, f)) and os.path.splitext(f)[1] == ".yaml"]
        files.sort(key=lambda f: int(os.path.splitext(f)[0]))
        files = [os.path.join(dir, f) for f in files]

        semester = Semester.objects.get(pk=semester_id)
        for file in files:
            with open(file) as f:
                courses = yaml.load(f)
            for c in courses:
                lessons = c.pop('lessons')
                course = Course(semester=semester, **c)
                course.save()
                for l in lessons:
                    l['weeks'] = list_to_comma_separated(l['weeks'])
                    lesson = Lesson(course=course, **l)
                    lesson.save()
            self.stdout.write('{}: successfully imported.\n'.format(file))