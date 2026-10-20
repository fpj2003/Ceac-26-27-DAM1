import json

agenda=[{
	"nombre":"Fernando",
	"apellidos":"Puig",
	"correo":"fpj2003@gmail.com"
	},
	{
	"nombre":"Juan",
	"apellidos":"Lopez",
	"correo":"juanlopez@gmail.com"
	},
	{
	"nombre":"Javier",
	"apellidos":"Garcia",
	"correo":"javigarcia@gmail.com"
	}
]

archivo = open("guardar.json",'w')
json.dump(agenda,archivo)
archivo.close()
