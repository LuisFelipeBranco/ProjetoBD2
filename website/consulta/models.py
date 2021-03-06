from django.db import models, connection


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=1)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aluno'

    def __str__(self):
        return self.nome

class AlunosTurma(models.Model):
    id_matricula = models.ForeignKey('Matricula', models.DO_NOTHING, db_column='id_matricula', primary_key = True)
    turma_periodo = models.ForeignKey('Turma', models.DO_NOTHING, db_column='turma_periodo', related_name='turma_periodo')
    turma_disciplina = models.ForeignKey('Turma', models.DO_NOTHING, db_column='turma_disciplina', related_name='turma_disciplina')

    class Meta:
        managed = False
        db_table = 'alunos_turma'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CadeirasCurso(models.Model):
    id_curso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='id_curso')
    id_disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='id_disciplina')
    OPTIONS_CHOICES = (
        ('0', 'V'),
        ('1', 'F'),
    )
    obrigatoria = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cadeiras_curso'

    @staticmethod
    def checar_obrigatoria(search_string):
        cur = connection.cursor()
        cur.callproc('curso_obrigatorias', [id])
        results = cur.fetchall()
        cur.close()
        return [CadeirasCurso(*row) for row in results]

class ConsultaAluno(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'consulta_aluno'


class ConsultaCurso(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=15)
    id_dpto = models.ForeignKey('ConsultaDepartamento', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'consulta_curso'


class ConsultaDepartamento(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=20)
    bloco = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'consulta_departamento'


class Curso(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    id_depto = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='id_depto')

    class Meta:
        managed = False
        db_table = 'curso'

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField(max_length=20)
    bloco = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=20, blank=True, null=True)
    id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_departamento')
    id_disciplina = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplina'

    def __str__(self):
        return self.nome

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Historico(models.Model):
    id = models.AutoField(primary_key=True)
    id_matricula = models.ForeignKey('Matricula', models.DO_NOTHING, db_column='id_matricula')
    id_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='id_disciplina')
    media = models.SmallIntegerField(blank=True, null=True)
    periodo = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'historico'


class Matricula(models.Model):
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno')
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso')
    id_tipo = models.ForeignKey('TipoIngresso', models.DO_NOTHING, db_column='id_tipo')
    id_situacao = models.ForeignKey('SituacaoMatricula', models.DO_NOTHING, db_column='id_situacao')

    class Meta:
        managed = False
        db_table = 'matricula'

class NotaAluno(models.Model):
    id = models.AutoField(primary_key=True)
    id_matricula = models.ForeignKey(Matricula, models.DO_NOTHING, db_column='id_matricula')
    id_professor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='id_professor')
    id_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='id_disciplina')
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso')
    nota1gq = models.SmallIntegerField(blank=True, null=True)
    nota2gq = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nota_aluno'

    def __str__(self):
        return '%s' % (self.id_matricula)

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=1)
    email = models.CharField(max_length=50)
    id_depto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_depto', blank=True, null=True)
    cfe = models.IntegerField(db_column='CFE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'professor'
        unique_together = (('id', 'cfe'),)

    def __str__(self):
        return self.nome

class SituacaoMatricula(models.Model):
    descricao = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'situacao_matricula'

    def __str__(self):
        return self.descricao

class TipoIngresso(models.Model):
    tipoingresso = models.CharField(db_column='tipoIngresso', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_ingresso'

    def __str__(self):
        return self.tipoingresso

class Turma(models.Model):
    periodo = models.SmallIntegerField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    id_professor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='id_professor')
    id_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='id_disciplina')
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso')

    class Meta:
        managed = False
        db_table = 'turma'
        unique_together = (('periodo', 'id_disciplina'),)

    def __str__(self):
        return self.nome