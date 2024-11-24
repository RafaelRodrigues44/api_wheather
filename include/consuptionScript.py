from django.shortcuts import render
from django.views import View
from gdacs.api import GDACSAPIReader

class Alert(View):
    def get(self, request):
        # Configurar o cliente da API do GDACS
        client = GDACSAPIReader()

        # Recuperar os 10 últimos eventos de alerta
        events = client.latest_events(limit=10)
        
        # Tratar o JSON recebido e separar cada objeto
        events_data = []
        for event in events.features:
            event_data = {
                'event_type': event['properties']['eventtype'],
                'event_id': event['properties']['eventid'],
                'episode_id': event['properties']['episodeid'],
                'event_name': event['properties']['name'],
                'description': event['properties']['description'],
                'html_description': event['properties']['htmldescription'],
                'icon': event['properties']['icon'],
                'icon_overall': event['properties']['iconoverall'],
                'url_geometry': event['properties']['url']['geometry'],
                'url_report': event['properties']['url']['report'],
                'url_details': event['properties']['url']['details'],
                'alert_level': event['properties']['alertlevel'],
                'alert_score': event['properties']['alertscore'],
                'episode_alert_level': event['properties']['episodealertlevel'],
                'episode_alert_score': event['properties']['episodealertscore'],
                'is_temporary': event['properties']['istemporary'],
                'is_current': event['properties']['iscurrent'],
                'country': event['properties']['country'],
                'from_date': event['properties']['fromdate'],
                'to_date': event['properties']['todate'],
                'date_modified': event['properties']['datemodified'],
                'iso3': event['properties']['iso3'],
                'source': event['properties']['source'],
                'source_id': event['properties']['sourceid'],
                'polygon_label': event['properties']['polygonlabel'],
                'class': event['properties']['Class'],
                'affected_countries': event['properties']['affectedcountries'],
                'severity': event['properties']['severitydata']['severity'],
                'severity_text': event['properties']['severitydata']['severitytext'],
                'severity_unit': event['properties']['severitydata']['severityunit']
            }
            events_data.append(event_data)

        # Renderizar o template alert.html com os dados dos alertas
        return render(request, 'alert.html', {'events_data': events_data})
