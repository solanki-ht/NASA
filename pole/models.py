from django.db import models
from django.db.models.signals import post_save
import random

# Create your models here.
class Minerals(models.Model):
   name=models.CharField(max_length=200,unique=True)
   def __unicode__(self):
      return str(self.name)

class Grid(models.Model):
   x_grid=models.IntegerField()
   y_grid=models.IntegerField()
   def __unicode__(self):
      return str(self.id)
  
class Subgrid(models.Model):
   sid_sub=models.ForeignKey('Grid')
   sx_sub=models.IntegerField()
   sy_sub=models.IntegerField()
   sid_key=models.IntegerField()
   def __unicode__(self):
      return 'G'+str(self.sid_sub)+"_"+'S'+str(self.sid_key)

class Rover(models.Model):
   x_rover=models.IntegerField()
   y_rover=models.IntegerField()
   h_rover=models.CharField(max_length=2)
   grid_rover=models.IntegerField()
   def __unicode__(self):
      return str('R'+str(self.id))
   
   def movement(self,r_str):
      for i in range(len(r_str)):


         if self.h_rover == 'N':
            if r_str[i] == 'M':
               self.y_rover = self.y_rover + 1
            elif r_str[i] == 'L':
               self.h_rover = 'W'
            else:
               self.h_rover = 'E'
         elif  self.h_rover == 'S':


            if r_str[i] == 'M':

               self.y_rover = self.y_rover - 1
            elif r_str[i] == 'L':

               self.h_rover = 'E'
            else:
               self.h_rover = 'W'
         elif self.h_rover == 'E':

            if r_str[i] == 'M':
               self.x_rover = self.x_rover + 1
            elif r_str[i]== 'L':
               self.h_rover = 'N'
            else:
               self.h_rover = 'S'
         else:
            if r_str[i] == 'M':
               self.y_rover = self.y_rover - 1
            elif r_str[i] == 'R':

               self.h_rover = 'N'
            else:
               self.h_rover = 'S' 
     # self.save()





class mineral_distri(models.Model):
   gid_min=models.ForeignKey('Grid')
   sid_min=models.ForeignKey('Subgrid')
   name_min=models.CharField(max_length=200)
   quant_min=models.IntegerField()
   def __unicode__(self):
      return str(self.sid_min)+str(self.name_min)


class searching_for(models.Model):
   rid=models.ForeignKey('Rover')
   mid=models.ForeignKey('Minerals')
   def __unicode__(self):
      return str(self.rid)+'_'+str(self.mid)
   
#post_save.connect(sub_grid,sender="grid")
#post_save.connect(distri,sender="Subgrid")
def sub_grid(sender,instance,**kwargs):
   t=0
   for i in range(int(instance.x_grid)):
      for j in range(int(instance.y_grid)):
         subgr=Subgrid()
         subgr.sid_sub=instance
         subgr.sx_sub=i
         subgr.sy_sub=j
         subgr.sid_key=t+1
         t=t+1
         subgr.save()

def distri(sender,instance,**kwargs):
   for i in range(5):
      min_dis=mineral_distri()
      min_dis.gid_min=instance.sid_sub
      min_dis.sid_min=instance
      min_dis.name_min='M'+str(i+1)
      ran=random.randint(0,2)
      if ran==0:
         min_dis.quant_min=0
      else:
         min_dis.quant_min=random.randint(3,11)
      min_dis.save()

#post_save.connect(distri,sender=Subgrid)  
post_save.connect(sub_grid,sender=Grid)
post_save.connect(distri,sender=Subgrid)



