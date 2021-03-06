from django.contrib.auth.models import User
from account.models import Costumer
from drug.models import Emchilgee
import django_filters

class EmchilgeeFilter(django_filters.FilterSet):
    class Meta:
        model = Emchilgee
        fields = ['costumer','onosh']

    def __init__(self, *args, **kwargs):
        super(EmchilgeeFilter, self).__init__(*args, **kwargs)
        self.filters['costumer'].label="Эмчлүүлэгч"
        self.filters['onosh'].label="Онош"

class CostumerFilter(django_filters.FilterSet):
    class Meta:
        model = Costumer
        fields = ['firstname', 'lastname', 'register']

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]
