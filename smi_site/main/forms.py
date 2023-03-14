# from django import forms

# MONTH_CHOICES=[('49', '1 месяц за 49₽'),('147', '3 месяца за 147₽'),('294', '6 месяцев за 294₽'),]
# KASSA_CHOISE=[('yk', ''),('fk', ''),]

# class BuysForm(forms.Form):
#     nick = forms.CharField(max_length=16, min_length=3, validators=[alphanumeric])
#     kassa = forms.CharField(widget=forms.RadioSelect(choices=KASSA_CHOISE))

# class PrimeBuyForm(forms.Form):
#     month = forms.CharField(label='Стоимость подписки 49₽ в месяц.', widget=forms.RadioSelect(choices=MONTH_CHOICES))
#     kassa = forms.CharField(widget=forms.RadioSelect(choices=KASSA_CHOISE))

# class UploadForm(forms.Form):
#     upload = forms.FileField(label='Выберите файл для загрузки: ')


from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()