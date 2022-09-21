from django import forms

COUNTRY=[('United States', 'United States'), ('other', 'other')]
STATE=[("AK","AK"), ("AL","AL"), ("AR","AR"), ("AZ","AZ"), ("CA","CA"), ("CO","CO"), ("CT","CT"), ("DC","DC"), ("DE","DE"), ("FL","FL"), ("GA","GA"),
 ("HI","HI"), ("IA","IA"), ("ID","ID"), ("IL","IL"), ("IN","IN"), ("KS","KS"), ("KY","KY"), ("LA","LA"), ("MA","MA"), ("MD","MD"), ("ME","ME"),
 ("MI","MI"), ("MN","MN"), ("MO","MO"), ("MS","MS"), ("MT","MT"), ("NC","NC"), ("ND","ND"), ("NE","NE"), ("NH","NH"), ("NJ","NJ"), ("NM","NM"), 
 ("NV","NV"), ("NY","NY"), ("OH","OH"), ("OK","OK"), ("OR","OR"), ("PA","PA"), ("RI","RI"), ("VT","VT"), ("SC","SC"), ("WI","WI"), ("SD","SD"), 
 ("TN","TN"), ("TX","TX"), ("UT","UT"), ("VA","VA"), ("WA","WA"), ("WV","WV"), ("WY","WY")]


class GetWeather(forms.Form):
    address = forms.CharField(label="Address")
    city = forms.CharField(label="City")
    state = forms.Select(label="State", choices=STATE)
    zip = forms.CharField(label="Zip")
    country = forms.Select(label='Country', choices=COUNTRY)