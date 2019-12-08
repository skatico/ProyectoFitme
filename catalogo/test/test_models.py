from catalogo.models import Usuario
from catalogo.models import Entrenador

class UsuarioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Usuario.objects.create(primer_nombre='robet', apellido='asffsa')

    def test_primer_nombre_label(self):
        usuario=Usuario.objects.get(id=1)
        field_label = usuario._meta.get_field('primer_nombre').verbose_name
        self.assertEquals(field_label,'primer_nombre')

    def test_fecha_nac(self):
        usuario=Usuario.objects.get(id=1)
        field_label = usuario._meta.get_field('fecha_nac').verbose_name
        self.assertEquals(field_label,'fecha_nac')

    def test_primer_nombre_max_length(self):
        usuario=Usuario.objects.get(id=1)
        max_length = usuario._meta.get_field('primer_nombre').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_apellido_comma_primer_nombre(self):
        usuario=Usuario.objects.get(id=1)
        expected_object_name = '%s, %s' %(usuario.apellido, usuario.primer_nombre)
        self.assertEquals(expected_object_name,str(usuario))

    def test_get_absolute_url(self):
        usuario=Usuario.objects.get(id=1)
        self.assertEquals(usuario.get_absolute_url(),'/catalogo/usuario/1')


class EntrenadorModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Entrenador.objects.create(primer_nombre='Pedro', apellido='Ferreira')

    def test_primer_nombre_label(self):
        entrenador=Entrenador.objects.get(id=1)
        field_label = entrenador._meta.get_field('primer_nombre').verbose_name
        self.assertEquals(field_label,'primer_nombre')

    def test_fecha_nac(self):
        entrenador=Entrenador.objects.get(id=1)
        field_label = entrenador._meta.get_field('fecha_nac').verbose_name
        self.assertEquals(field_label,'fecha_nac')

    def test_primer_nombre_max_length(self):
        entrenador=Entrenador.objects.get(id=1)
        max_length = entrenador._meta.get_field('primer_nombre').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_apellido_comma_primer_nombre(self):
        entrenador=Entrenador.objects.get(id=1)
        expected_object_name = '%s, %s' %(entrenador.apellido, entrenador.primer_nombre)
        self.assertEquals(expected_object_name,str(entrenador))

    def test_get_absolute_url(self):
        entrenador=Entrenador.objects.get(id=1)
        self.assertEquals(entrenador.get_absolute_url(),'/catalogo/entrenador/1')