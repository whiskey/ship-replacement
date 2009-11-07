'''
Created on Oct 19, 2009

@author: carsten
'''
from django.db import models
import locale

class Ticket(models.Model):
    date_entry = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateTimeField(auto_now_add=True)
    issuer = models.CharField(max_length=50)
    victim = models.CharField(max_length=50)
    ship = models.CharField(max_length=60)
    kbLink = models.CharField(max_length=150, blank=True)
    statusOpen = models.BooleanField()
    notes = models.CharField(max_length=500, blank=True)
    
    def __unicode__(self):
        return "%s: %s lost %s (open ticket: %s)" % (self.date_entry, self.victim, self.ship, self.statusOpen)
    
    class Meta:
        permissions = (
                       ('can_close_tickets', 'is able to payout players and close the ticket'),
                       )
        ordering = ['-date_entry']


class ShipPrice(models.Model):
    type = models.CharField(max_length=100)
    value = models.IntegerField()
    
    def __unicode__(self):
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        val = locale.format('%d',self.value, True)
        return "%(type)s - %(value)s ISK" % {'type':self.type, 'value':val}
    
    class Meta:
        #ordering = ['value']
        pass
