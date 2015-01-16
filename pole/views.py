from django.http import HttpResponse
#from django.db.models.signals
from models import *
from django.shortcuts import render
from form import *
def solanki(request):
   return HttpResponse('Hii solanki')
def menu(request):
	return render(request,"menu_form.html")
def Grid_view(request):
   
   if request.method=='POST':
      g=Grid()
      g.x_grid=request.POST['x_grid']
      g.y_grid=request.POST['y_grid']
      g.save()
      
   else:
      gform=GridForm()
      return render(request,"grid_form.html",{"form":gform})
   return render(request,"gr_form.html")
def Rover_view(request):
   if request.method=='POST':
      r=Rover()
      r.x_rover=request.POST['x_rover']
      r.y_rover=request.POST['y_rover']
      r.h_rover=request.POST['h_rover']
      r.grid_rover=request.POST['grid_rover']
      #r.grid_rover=Grid.objects.filter(id=gid_rover)[0]
      r.save()
   else:
      rform=RoverForm()
      return render(request,"rover_form.html",{"form":rform})
   return render(request,"rov_form.html")

def rover_move(request):


    if request.method=='POST':
        rov_id=request.POST['rover_id']
        rov_direc=request.POST['move_string']
        inst=Rover.objects.filter(id=rov_id)[0]
        inst.movement(rov_direc)
        st='final-x='+' '+str(inst.x_rover)+'     '+'final-y='+' '+str(inst.y_rover)+'     '+'direction='+' '+str(inst.h_rover)
        return HttpResponse(st)
    else:
        return  render(request,"move_form.html")
    

def sensor(request):
	if request.method=='POST':
		sense=searching_for()
		rid=request.POST['rid']
		sense.rid=Rover.objects.filter(id=rid)[0]
		mid=request.POST['mid']
		sense.mid=Minerals.objects.filter(id=mid)[0]
		sense.save()
	else:
		sense=SensorForm()
		return render(request,"sense_form.html",{"form":sense})
	return render(request,"sen_form.html")

def rover_update_form1(request):
	if request.method=='POST':
		form = rover_update_form(request.POST)
		rov_id=request.POST['rid']
		inst=Rover.objects.filter(id=rov_id)[0]
		inst.x_rover=request.POST['x_rover']
		inst.y_rover=request.POST['y_rover']
		inst.h_rover=request.POST['h_rover']
		gid=request.POST['gid']
		ib=Grid.objects.filter(id=gid)[0]
		inst.grid_rover=ib
		inst.save()
	else:
		form = rover_update_form()
	c = {'form':form}
	return render(request,'update.html',c)
def new_mineral1(request):
	if request.method=='POST':
		#form = new_mineral(request.POST)
		mrl=Minerals()
		mr=request.POST['name']
		if len(Minerals.objects.filter(name=mr))>0:
			return render(request,"tt_form.html")
		else:
			mrl.name=mr
			mrl.save()
		return render(request,"min_form.html")
	else:
		rform=new_mineral_form()
		return render(request,"mineral_form.html",{"form":rform})
    



  

# Create your views here.
