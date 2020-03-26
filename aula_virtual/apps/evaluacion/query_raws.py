from django.db import connection

def traer_examenes(self,id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchall()
    return row