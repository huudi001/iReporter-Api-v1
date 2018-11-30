incidents = []

class IncidentsData():
   def save_incident(self, created_on ,created_by, type, location , status, images, videos, comment):
       incidentId = len(incidents)+1

       user_incidents = {
           "incidentId":incidentId,
           "created_on":created_on,
           "created_by":created_by,
           "type":type,
           "location":location,
           "status":status,
           "images":[],
           "videos":[],
           "comment":comment
        }
       incidents.append(user_incidents)

       return user_incidents

   def get_incidents(self):
       return incidents
