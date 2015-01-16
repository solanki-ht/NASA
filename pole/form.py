from django.forms import ModelForm
from django import forms
from models import Grid,Subgrid,Minerals,Rover,searching_for
class GridForm(ModelForm):
	class Meta:
		model=Grid
		field='__all__'
class RoverForm(ModelForm):
	class Meta:
		model=Rover
		field='__all__'
class SensorForm(ModelForm):
	class Meta:
		model=searching_for
		field='__all__'
class rover_update_form(forms.Form):
	rid=forms.IntegerField(label='rover_id')
	x_rover=forms.IntegerField(label='x_position')
	y_rover=forms.IntegerField(label='y_position')
	h_rover=forms.CharField(label='direction')
	gid=forms.IntegerField(label='new_grid_id')

class new_mineral_form(ModelForm):
	class Meta:
		model=Minerals
		field='__all__'


