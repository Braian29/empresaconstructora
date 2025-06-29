import os
from django.core.files.base import ContentFile
from django.conf import settings
from django.db import IntegrityError

# Importa todos tus modelos desde sus respectivas apps
from core.models import ContactInfo
from about.models import TeamMember, Value, Testimonial, AboutUs
from services.models import ServiceCategory, Service
from projects.models import ProjectCategory, Project, ProjectImage

# --- Configuración de imágenes de prueba ---
# Un GIF transparente de 1x1 píxel en base64. Esto simula una imagen sin necesidad de tener archivos reales.
# Lo ideal sería usar imágenes representativas reales en un entorno de producción.
DUMMY_IMAGE_DATA = b"R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="

# --- Funciones de carga de datos ---

def load_contact_info():
    print("Cargando información de contacto...")
    # Siempre intenta crear o actualizar la única instancia de ContactInfo
    contact_info, created = ContactInfo.objects.get_or_create(
        phone_number='+54 9 11 2637-0364', # Campo usado para la búsqueda de `get_or_create`
        defaults={
            'address': 'Av. Corrientes 1234, CABA, Argentina',
            'email': 'constructora.lework@hotmail.com',
            'instagram': 'https://www.instagram.com/constructora.lework/',
            'latitude': -34.6037, # Latitud del Obelisco, CABA (ejemplo)
            'longitude': -58.3816, # Longitud del Obelisco, CABA (ejemplo)
            'schedule': 'Lunes a Viernes de 9:00 a 18:00',
        }
    )
    if created:
        print(f"  Información de contacto creada: {contact_info.email}")
    else:
        print(f"  Información de contacto ya existe: {contact_info.email}. Actualizando...")
        # Si ya existe, asegúrate de que los valores por defecto estén actualizados
        contact_info.address = 'Av. Corrientes 1234, CABA, Argentina'
        contact_info.email = 'constructora.lework@hotmail.com'
        contact_info.instagram = 'https://www.instagram.com/constructora.lework/'
        contact_info.latitude = -34.6037
        contact_info.longitude = -58.3816
        contact_info.schedule = 'Lunes a Viernes de 9:00 a 18:00'
        contact_info.save()

def load_team_members():
    print("Cargando miembros del equipo...")
    members_data = [
        {
            'name': 'Sergio Casal',
            'title': 'Fundador y Director General',
            'bio': 'Con más de 22 años de experiencia en el rubro, lidera cada proyecto con pasión y compromiso, asegurando la visión y los valores de LE WORK Constructora. Su presencia activa garantiza la calidad y la cercanía en cada obra.',
            'image_name': 'sergio_casal.jpg'
        },
        {
            'name': 'Betania Farrazzano',
            'title': 'Consultora Estratégica',
            'bio': 'A cargo de la consultoría estratégica y la comunicación, Betania asegura que la visión y los valores de la empresa se transmitan con claridad y que la relación con cada cliente sea transparente y efectiva.',
            'image_name': 'betania_farrazzano.jpg'
        },
        {
            'name': 'Equipo Técnico LE WORK',
            'title': 'Arquitectos e Ingenieros',
            'bio': 'Nuestro equipo de profesionales expertos en arquitectura e ingeniería garantiza la excelencia técnica, la innovación y la seguridad en cada obra, desde la planificación hasta la entrega final, transformando ideas en realidad con precisión.',
            'image_name': 'team_lework.jpg'
        },
    ]
    team_members_map = {}
    for data in members_data:
        member, created = TeamMember.objects.get_or_create(
            name=data['name'],
            defaults={
                'title': data['title'],
                'bio': data['bio']
            }
        )
        if created:
            print(f"  Miembro '{member.name}' creado.")
            if data['image_name']:
                # Simula la carga de una imagen
                member.image.save(data['image_name'], ContentFile(DUMMY_IMAGE_DATA), save=True)
        else:
            print(f"  Miembro '{member.name}' ya existe.")
            # Opcional: Actualizar campos si ya existía
            member.title = data['title']
            member.bio = data['bio']
            if not member.image and data['image_name']: # Solo cargar si no hay imagen
                 member.image.save(data['image_name'], ContentFile(DUMMY_IMAGE_DATA), save=True)
            member.save() # Guarda los cambios si se actualizó
        team_members_map[data['name']] = member
    return team_members_map

def load_values():
    print("Cargando valores...")
    values_data = [
        {
            'name': 'Compromiso familiar',
            'description': 'Nos involucramos personalmente desde temprano, con presencia activa del dueño, la esposa y los hijos en cada etapa del proyecto, asegurando una dedicación integral.',
            'icon_name': 'icon_family.png'
        },
        {
            'name': 'Cercanía y dedicación al cliente',
            'description': 'Mantenemos una comunicación constante y reuniones periódicas para que cada cliente se sienta parte de su propia obra, resolviendo dudas y ajustando detalles.',
            'icon_name': 'icon_client_focus.png'
        },
        {
            'name': 'Calidad sin importar la escala',
            'description': 'Cada proyecto es tomado como un nuevo desafío, con el mismo nivel de planificación y ejecución profesional, garantizando acabados de primera sin importar el tamaño.',
            'icon_name': 'icon_quality.png'
        },
        {
            'name': 'Seguimiento real y transparente',
            'description': 'Mostramos el avance de cada obra con fotos y videos semanales, brindando total transparencia y tranquilidad a nuestros clientes sobre el progreso de su inversión.',
            'icon_name': 'icon_transparency.png'
        },
        {
            'name': 'Ética profesional',
            'description': 'Aunque estamos abiertos a propuestas de los clientes, respetamos siempre los límites legales, técnicos y de seguridad constructiva, asegurando la integridad y la sostenibilidad de cada edificación.',
            'icon_name': 'icon_ethics.png'
        },
    ]
    values_map = {}
    for data in values_data:
        value, created = Value.objects.get_or_create(
            name=data['name'],
            defaults={'description': data['description']}
        )
        if created:
            print(f"  Valor '{value.name}' creado.")
            if data['icon_name']:
                value.icon.save(data['icon_name'], ContentFile(DUMMY_IMAGE_DATA), save=True)
        else:
            print(f"  Valor '{value.name}' ya existe.")
            value.description = data['description']
            if not value.icon and data['icon_name']:
                value.icon.save(data['icon_name'], ContentFile(DUMMY_IMAGE_DATA), save=True)
            value.save() # Guarda los cambios si se actualizó
        values_map[data['name']] = value
    return values_map

def load_testimonials():
    print("Cargando testimonios generales...")
    testimonials_data = [
        {
            'client_name': 'Ana G.',
            'content': 'LE WORK transformó nuestra casa en el hogar de nuestros sueños. Su profesionalismo y atención al detalle fueron excepcionales desde el primer contacto hasta la entrega de llaves. ¡Totalmente recomendados!',
            'image_name': 'client_ana.jpg'
        },
        {
            'client_name': 'Carlos R., CEO de Industrias Alpha',
            'content': 'La construcción de nuestra nueva planta industrial fue un desafío, pero LE WORK lo manejó con una eficiencia y calidad que superaron nuestras expectativas. Un equipo comprometido y con visión.',
            'image_name': 'client_carlos.jpg'
        },
        {
            'client_name': 'Familia Rodríguez',
            'content': 'La reforma de nuestra cocina y baños fue impecable. Los resultados son fantásticos y el proceso fue muy transparente, con comunicación constante. Estamos muy felices con el trabajo de LE WORK.',
            'image_name': 'client_rodriguez.jpg'
        },
    ]
    testimonials_list = []
    for data in testimonials_data:
        # Se usa client_name y content para la unicidad, aunque idealmente se necesitaría un campo unique=True
        # o una lógica más compleja para evitar duplicados si los contenidos son muy similares.
        testimonial, created = Testimonial.objects.get_or_create(
            client_name=data['client_name'],
            content=data['content'] # Considera usar un hash del contenido o un campo único si se repiten nombres
        )
        if created:
            print(f"  Testimonio de '{testimonial.client_name}' creado.")
            if data['image_name']:
                testimonial.image.save(data['image_name'], ContentFile(DUMMY_IMAGE_DATA), save=True)
        else:
            print(f"  Testimonio de '{testimonial.client_name}' ya existe.")
            if not testimonial.image and data['image_name']:
                testimonial.image.save(data['image_name'], ContentFile(DUMMY_IMAGE_DATA), save=True)
            testimonial.save() # Guarda por si se actualizó la imagen
        testimonials_list.append(testimonial)
    return testimonials_list

def load_about_us(team_members_map, values_map, testimonials_list):
    print("Cargando sección 'Quiénes Somos'...")
    # get_or_create para la única instancia de AboutUs
    about_us, created = AboutUs.objects.get_or_create(
        title="Quiénes Somos", # Usamos el título como campo de búsqueda para la única instancia
        defaults={
            'main_content': 'Somos una empresa constructora familiar con más de 22 años en el rubro. Nos especializamos en la ejecución de obras residenciales, industriales y comerciales, ofreciendo un servicio integral que incluye dirección técnica, ingeniería y arquitectura. Nuestro compromiso con la calidad, el seguimiento personalizado y la cercanía con cada cliente nos permite acompañar cada proyecto desde la planificación hasta la entrega final.',
            'mission': 'Acompañamos a cada cliente en la construcción de su proyecto, brindando seguimiento personalizado, comunicación constante y un equipo técnico comprometido con la calidad. Nuestra misión es que cada obra, sin importar su escala o sistema constructivo, sea tratada con la misma dedicación y planificación, asegurando que cada peso invertido esté justificado. Nos enorgullece entregar obras limpias, bien ejecutadas y que reflejen el sueño de quienes confiaron en nosotros, desde la primera reunión hasta la entrega final.',
            'vision': 'Ser reconocidos como una constructora confiable, profesional y cercana, que deja huella en cada obra por su calidad y compromiso. Queremos que quienes trabajaron con nosotros nos recomienden con orgullo, sabiendo que cumplimos lo prometido, respetamos los tiempos y acompañamos al cliente en cada etapa. Aspiramos a seguir creciendo como empresa familiar, sumando obras que nos desafíen y consolidando un equipo técnico que mantenga nuestros valores en cada proyecto.',
        }
    )
    if created:
        print("  Sección 'Quiénes Somos' creada.")
    else:
        print("  Sección 'Quiénes Somos' ya existe. Actualizando contenido principal...")
        # Asegurarse de que el contenido se actualice incluso si ya existía
        about_us.main_content = 'Somos una empresa constructora familiar con más de 22 años en el rubro. Nos especializamos en la ejecución de obras residenciales, industriales y comerciales, ofreciendo un servicio integral que incluye dirección técnica, ingeniería y arquitectura. Nuestro compromiso con la calidad, el seguimiento personalizado y la cercanía con cada cliente nos permite acompañar cada proyecto desde la planificación hasta la entrega final.'
        about_us.mission = 'Acompañamos a cada cliente en la construcción de su proyecto, brindando seguimiento personalizado, comunicación constante y un equipo técnico comprometido con la calidad. Nuestra misión es que cada obra, sin importar su escala o sistema constructivo, sea tratada con la misma dedicación y planificación, asegurando que cada peso invertido esté justificado. Nos enorgullece entregar obras limpias, bien ejecutadas y que reflejen el sueño de quienes confiaron en nosotros, desde la primera reunión hasta la entrega final.'
        about_us.vision = 'Ser reconocidos como una constructora confiable, profesional y cercana, que deja huella en cada obra por su calidad y compromiso. Queremos que quienes trabajaron con nosotros nos recomienden con orgullo, sabiendo que cumplimos lo prometido, respetamos los tiempos y acompañamos al cliente en cada etapa. Aspiramos a seguir creciendo como empresa familiar, sumando obras que nos desafíen y consolidando un equipo técnico que mantenga nuestros valores en cada proyecto.'
        about_us.save()

    # Añadir las relaciones ManyToMany
    # Siempre se usa .set() para asegurar que las relaciones sean exactamente las que se definen aquí.
    about_us.values.set(list(values_map.values())) # Añade todos los valores creados
    print("  Valores asociados a 'Quiénes Somos'.")
    
    about_us.team_members.set([
        team_members_map['Sergio Casal'],
        team_members_map['Betania Farrazzano'],
        team_members_map['Equipo Técnico LE WORK']
    ])
    print("  Miembros del equipo asociados a 'Quiénes Somos'.")

    about_us.testimonials.set(testimonials_list) # Añade todos los testimonios generales
    print("  Testimonios asociados a 'Quiénes Somos'.")

def load_service_categories():
    print("Cargando categorías de servicio...")
    categories_data = [
        {'name': 'Obras residenciales', 'icon_name': 'icon_residential.png'},
        {'name': 'Obras industriales y grandes superficies', 'icon_name': 'icon_industrial.png'},
        {'name': 'Movimiento de suelos', 'icon_name': 'icon_soil.png'},
        {'name': 'Servicios complementarios', 'icon_name': 'icon_complementary.png'},
        {'name': 'Dirección técnica y gestión integral', 'icon_name': 'icon_technical.png'},
    ]
    categories_map = {}
    for data in categories_data:
        category, created = ServiceCategory.objects.get_or_create(
            name=data['name'],
            defaults={'description': f"Categoría de servicios relacionados con {data['name'].lower()}"}
        )
        if created:
            print(f"  Categoría de servicio '{category.name}' creada.")
            if data['icon_name']:
                category.icon.save(data['icon_name'], ContentFile(DUMMY_IMAGE_DATA), save=True)
        else:
            print(f"  Categoría de servicio '{category.name}' ya existe.")
            # Opcional: Actualizar descripción si ya existía
            category.description = f"Categoría de servicios relacionados con {data['name'].lower()}"
            if not category.icon and data['icon_name']:
                 category.icon.save(data['icon_name'], ContentFile(DUMMY_IMAGE_DATA), save=True)
            category.save()
        categories_map[data['name']] = category
    return categories_map

def load_services(service_categories_map):
    print("Cargando servicios...")
    
    services_data = [
        # Obras residenciales
        {
            'category_name': 'Obras residenciales',
            'title': 'Viviendas unifamiliares en sistema tradicional.',
            'short_description': 'Construcción de hogares sólidos y duraderos con métodos tradicionales.',
            'description': 'Nos especializamos en la construcción de viviendas unifamiliares utilizando sistemas tradicionales de ladrillo y hormigón, asegurando resistencia, eficiencia y confort. Nuestro servicio incluye asesoramiento profesional, dirección técnica y honorarios de arquitectos incorporados en el valor final.',
            'image_name': 'service_traditional_home.jpg'
        },
        {
            'category_name': 'Obras residenciales',
            'title': 'Viviendas en steel framing (obra en seco).',
            'short_description': 'Soluciones modernas y rápidas con construcción en seco de alta calidad.',
            'description': 'Ofrecemos la construcción de viviendas con sistema Steel Framing, un método innovador que permite reducir tiempos de obra, minimizar residuos y obtener una construcción ligera y resistente, ideal para diseños modernos. Incluye asesoramiento y dirección técnica.',
            'image_name': 'service_steel_framing.jpg'
        },
        {
            'category_name': 'Obras residenciales',
            'title': 'Proyectos de inversión: Casa + Terreno.',
            'short_description': 'Inversiones inmobiliarias llave en mano, optimizando el retorno de tu capital.',
            'description': 'Desarrollamos proyectos de inversión que combinan la adquisición del terreno con la construcción de una vivienda, ofreciendo una solución llave en mano para inversores que buscan rentabilidad y seguridad. Gestión integral desde la búsqueda del terreno hasta la entrega del inmueble.',
            'image_name': 'service_investment.jpg'
        },
        {
            'category_name': 'Obras residenciales',
            'title': 'Ampliaciones y reformas integrales.',
            'short_description': 'Transforma y moderniza tus espacios existentes con soluciones personalizadas.',
            'description': 'Realizamos ampliaciones y reformas integrales para actualizar, modernizar o adaptar tus espacios existentes a nuevas necesidades. Desde la planificación hasta la ejecución, garantizamos un trabajo de calidad que respeta la estructura original y optimiza la funcionalidad y estética.',
            'image_name': 'service_reforms.jpg'
        },
        {
            'category_name': 'Obras residenciales',
            'title': 'Construcción de piscinas con solarium.',
            'short_description': 'Diseño y construcción de piscinas que complementan tu hogar y estilo de vida.',
            'description': 'Construimos piscinas a medida, incluyendo diseños personalizados y solariums integrados, utilizando materiales de alta durabilidad y tecnología de filtrado avanzada. Creamos un espacio de esparcimiento que añade valor y belleza a tu propiedad.',
            'image_name': 'service_pools.jpg'
        },
        # Obras industriales y grandes superficies
        {
            'category_name': 'Obras industriales y grandes superficies',
            'title': 'Construcción de fábricas industriales.',
            'short_description': 'Infraestructura industrial robusta y funcional para tu producción.',
            'description': 'Desarrollamos proyectos de construcción de fábricas industriales, adaptándonos a las necesidades específicas de cada sector. Nuestro enfoque garantiza la optimización de espacios, la seguridad operativa y la eficiencia en los procesos productivos.',
            'image_name': 'service_factory.jpg'
        },
        {
            'category_name': 'Obras industriales y grandes superficies',
            'title': 'Construcción de edificios corporativos o multifamiliares.',
            'short_description': 'Edificios modernos y eficientes para uso corporativo o residencial.',
            'description': 'Diseñamos y construimos edificios corporativos y multifamiliares, ofreciendo soluciones arquitectónicas innovadoras y funcionales. Nos comprometemos con la creación de espacios que fomentan la productividad y el bienestar, con altos estándares de calidad y sostenibilidad.',
            'image_name': 'service_corporate_building.jpg'
        },
        {
            'category_name': 'Obras industriales y grandes superficies',
            'title': 'Estructuras de hormigón armado.',
            'short_description': 'Construcción de estructuras de hormigón armado, base de obras sólidas y seguras.',
            'description': 'Especialistas en el cálculo y ejecución de estructuras de hormigón armado, garantizando la solidez y durabilidad de todo tipo de construcciones. Desde cimientos hasta elementos estructurales complejos, aseguramos la máxima resistencia y seguridad.',
            'image_name': 'service_concrete_structure.jpg'
        },
        # Movimiento de suelos
        {
            'category_name': 'Movimiento de suelos',
            'title': 'Nivelación, compactación y apertura de suelo.',
            'short_description': 'Preparación profesional del terreno para una base sólida.',
            'description': 'Realizamos trabajos de nivelación, compactación y apertura de suelo, fundamentales para asegurar la estabilidad y el correcto asiento de cualquier edificación. Contamos con maquinaria y personal especializado para una preparación óptima del terreno.',
            'image_name': 'service_soil_leveling.jpg'
        },
        {
            'category_name': 'Movimiento de suelos',
            'title': 'Excavaciones profundas o técnicas.',
            'short_description': 'Excavaciones precisas y seguras para cimientos y subsuelos.',
            'description': 'Ofrecemos servicios de excavaciones profundas y técnicas, adaptándonos a la complejidad de cada proyecto y a las características del terreno. Garantizamos la seguridad y la precisión necesarias para la creación de cimientos, sótanos y otras estructuras subterráneas.',
            'image_name': 'service_excavation.jpg'
        },
        {
            'category_name': 'Movimiento de suelos',
            'title': 'Retiros de escombros.',
            'short_description': 'Gestión eficiente y responsable de residuos de obra.',
            'description': 'Nos encargamos del retiro de escombros y materiales de desecho de la obra de forma eficiente y responsable, asegurando el cumplimiento de normativas ambientales y manteniendo el sitio de trabajo limpio y organizado.',
            'image_name': 'service_debris_removal.jpg'
        },
        # Servicios complementarios
        {
            'category_name': 'Servicios complementarios',
            'title': 'Instalación de cloacas.',
            'short_description': 'Instalaciones sanitarias completas y conformes a normativa.',
            'description': 'Realizamos instalaciones completas de sistemas de cloacas y saneamiento, garantizando la funcionalidad, la seguridad y el cumplimiento de todas las normativas vigentes. Un servicio esencial para la habitabilidad de cualquier edificación.',
            'image_name': 'service_sewage.jpg'
        },
        {
            'category_name': 'Servicios complementarios',
            'title': 'Carga y entrega de materiales a obra.',
            'short_description': 'Logística de materiales eficiente para tu proyecto.',
            'description': 'Gestionamos la carga y entrega de materiales de construcción directamente en la obra, asegurando la disponibilidad oportuna de los insumos necesarios y optimizando los tiempos de ejecución del proyecto. Una solución logística integral.',
            'image_name': 'service_material_delivery.jpg'
        },
        {
            'category_name': 'Servicios complementarios',
            'title': 'Hormigonado.',
            'short_description': 'Servicios de hormigonado profesional y de alta calidad.',
            'description': 'Ofrecemos servicios de hormigonado para todo tipo de estructuras, desde plateas y losas hasta columnas y vigas. Utilizamos hormigón de calidad y técnicas avanzadas para garantizar la resistencia y durabilidad de los elementos constructivos.',
            'image_name': 'service_concreting.jpg'
        },
        # Dirección técnica y gestión integral
        {
            'category_name': 'Dirección técnica y gestión integral',
            'title': 'Equipo interno de arquitectos e ingenieros para cada tipo de proyecto.',
            'short_description': 'Expertos en cada área para una dirección técnica precisa.',
            'description': 'Contamos con un equipo multidisciplinario de arquitectos e ingenieros internos, especializados en diferentes tipos de proyectos (residenciales, industriales, comerciales). Aseguramos la dirección técnica y el control de calidad en cada fase de la obra.',
            'image_name': 'service_dt_team.jpg'
        },
        {
            'category_name': 'Dirección técnica y gestión integral',
            'title': 'Dirección técnica incluida en obras llave en mano.',
            'short_description': 'Servicio de dirección técnica sin costos adicionales en proyectos llave en mano.',
            'description': 'Para nuestros proyectos "llave en mano", la dirección técnica profesional está incluida en el presupuesto final. Esto garantiza una gestión integral sin sorpresas, con un único interlocutor y la máxima eficiencia en cada etapa.',
            'image_name': 'service_dt_included.jpg'
        },
        {
            'category_name': 'Dirección técnica y gestión integral',
            'title': 'Proyectos 100% gestionados por la empresa.',
            'short_description': 'Gestión integral y sin preocupaciones para tu proyecto.',
            'description': 'Nos hacemos cargo de la gestión completa de tu proyecto, desde la planificación inicial y la obtención de permisos hasta la ejecución y la entrega final. Una solución integral que te libera de preocupaciones y garantiza un control total del proceso.',
            'image_name': 'service_full_management.jpg'
        },
    ]

    all_services = []
    for data in services_data:
        category = service_categories_map.get(data['category_name'])
        if not category:
            print(f"  Advertencia: Categoría '{data['category_name']}' no encontrada para el servicio '{data['title']}'. Saltando.")
            continue
        
        service, created = Service.objects.get_or_create(
            title=data['title'],
            defaults={
                'category': category,
                'short_description': data['short_description'],
                'description': data['description']
            }
        )
        if created:
            print(f"  Servicio '{service.title}' creado.")
            if data['image_name']:
                service.image.save(data['image_name'], ContentFile(DUMMY_IMAGE_DATA), save=True)
        else:
            print(f"  Servicio '{service.title}' ya existe.")
            # Opcional: Actualizar campos si ya existía
            service.category = category
            service.short_description = data['short_description']
            service.description = data['description']
            if not service.image and data['image_name']:
                service.image.save(data['image_name'], ContentFile(DUMMY_IMAGE_DATA), save=True)
            service.save()
        all_services.append(service)
    return all_services

def load_project_categories():
    print("Cargando categorías de proyecto...")
    categories_data = [
        {'name': 'Residencial'},
        {'name': 'Industrial'}, # Incluye comercial/oficinas para el ejemplo
        {'name': 'Reforma'},
        {'name': 'Steel Framing'},
        {'name': 'Piscinas'},
        {'name': 'Tradicional'},
    ]
    categories_map = {}
    for data in categories_data:
        category, created = ProjectCategory.objects.get_or_create(name=data['name'])
        if created:
            print(f"  Categoría de proyecto '{category.name}' creada.")
        else:
            print(f"  Categoría de proyecto '{category.name}' ya existe.")
        categories_map[data['name']] = category
    return categories_map

def load_projects(project_categories_map, all_services):
    print("Cargando proyectos...")
    
    # Crea un mapa de servicios por su título para una búsqueda fácil
    service_map = {s.title: s for s in all_services}

    projects_data = [
        {
            'title': 'Residencia "La Arboleda"',
            'short_description': 'Vivienda unifamiliar moderna con diseño minimalista y amplios espacios verdes.',
            'detailed_description': 'Proyecto llave en mano que incluyó la construcción de una residencia de 250m² con sistema tradicional, 3 dormitorios, piscina y quincho. Se destacó el diseño de jardinería y la integración con el entorno natural, creando un hogar luminoso y conectado con la naturaleza.',
            'categories': ['Residencial', 'Tradicional', 'Piscinas'],
            'services_used': [
                'Viviendas unifamiliares en sistema tradicional.',
                'Construcción de piscinas con solarium.',
                'Dirección técnica incluida en obras llave en mano.'
            ],
            'client': 'Familia Pérez',
            'location': 'Barrio Cerrado Las Rosas, Buenos Aires',
            'duration': '10 meses',
            'service_type': 'Construcción llave en mano',
            'client_testimonial_quote': 'Estamos encantados con nuestra nueva casa. Superó todas nuestras expectativas y el equipo de LE WORK fue increíble. Su compromiso familiar se notó en cada detalle.',
            'client_testimonial_author': 'Laura y Juan Pérez',
            'images': [
                {'name': 'project_arboleda_main.jpg', 'is_main': True, 'caption': 'Fachada principal y acceso vehicular'},
                {'name': 'project_arboleda_pool.jpg', 'is_main': False, 'caption': 'Piscina y solárium con vistas al jardín'},
                {'name': 'project_arboleda_interior.jpg', 'is_main': False, 'caption': 'Interior luminoso y espacioso'},
            ]
        },
        {
            'title': 'Casa "Vista al Lago"',
            'short_description': 'Diseño vanguardista con foco en la iluminación natural y vistas panorámicas.',
            'detailed_description': 'Proyecto de construcción de 200m² en Steel Framing, incluyendo una gran piscina con solárium y áreas de estar al aire libre. La planificación optimizó la eficiencia energética y los tiempos de ejecución, logrando un diseño moderno y funcional con vistas espectaculares al lago.',
            'categories': ['Residencial', 'Steel Framing', 'Piscinas'],
            'services_used': [
                'Viviendas en steel framing (obra en seco).',
                'Construcción de piscinas con solarium.',
                'Proyectos 100% gestionados por la empresa.'
            ],
            'client': 'Matías G.',
            'location': 'Pueblo Chico, Zona Norte',
            'duration': '8 meses',
            'service_type': 'Construcción en seco + exteriores',
            'client_testimonial_quote': 'Una obra limpia y rápida. No puedo creer lo rápido que tuvimos nuestra casa lista sin sacrificar calidad. El seguimiento fue constante y la comunicación excelente.',
            'client_testimonial_author': 'Matías G.',
            'images': [
                {'name': 'project_vista_lago_main.jpg', 'is_main': True, 'caption': 'Vista frontal de la casa moderna'},
                {'name': 'project_vista_lago_patio.jpg', 'is_main': False, 'caption': 'Patio trasero y zona de piscina'},
                {'name': 'project_vista_lago_living.jpg', 'is_main': False, 'caption': 'Living con grandes ventanales'},
            ]
        },
        {
            'title': 'Reforma Integral "Oficinas Centro"',
            'short_description': 'Modernización completa de espacio de oficinas con diseño funcional.',
            'detailed_description': 'Proyecto de reforma integral de 300m² para un estudio de abogados en el centro de la ciudad. Se renovó por completo la distribución, las instalaciones eléctricas y sanitarias, y se implementó un diseño moderno y abierto para fomentar la colaboración y la productividad. El desafío principal fue ejecutar la obra sin interrumpir las operaciones del cliente.',
            'categories': ['Industrial', 'Reforma'],
            'services_used': [
                'Ampliaciones y reformas integrales.',
                'Equipo interno de arquitectos e ingenieros para cada tipo de proyecto.',
                'Retiros de escombros.'
            ],
            'client': 'Estudio Jurídico "LexCorp"',
            'location': 'Microcentro, CABA',
            'duration': '4 meses',
            'service_type': 'Remodelación y equipamiento',
            'client_testimonial_quote': 'El equipo de LE WORK fue increíble. Pudieron reformar nuestras oficinas con la mínima interrupción a nuestro trabajo y el resultado final superó con creces lo que imaginábamos. ¡Profesionalismo puro!',
            'client_testimonial_author': 'Dr. Marcos Silva, Socio Gerente',
            'images': [
                {'name': 'project_offices_main.jpg', 'is_main': True, 'caption': 'Oficina principal renovada'},
                {'name': 'project_offices_meeting.jpg', 'is_main': False, 'caption': 'Sala de reuniones moderna'},
                {'name': 'project_offices_hall.jpg', 'is_main': False, 'caption': 'Hall de entrada antes y después'},
            ]
        },
    ]

    for data in projects_data:
        # Usamos el título como criterio para get_or_create
        # Si el slug se genera en Project.save(), el get_or_create necesita un 'lookup' que coincida
        # En este caso, el slug se genera del título, así que si el título es único, el slug también lo será
        project, created = Project.objects.get_or_create(
            title=data['title'],
            defaults={
                'short_description': data['short_description'],
                'detailed_description': data['detailed_description'],
                'client': data.get('client'),
                'location': data.get('location'),
                'duration': data.get('duration'),
                'service_type': data.get('service_type'),
                'client_testimonial_quote': data.get('client_testimonial_quote'),
                'client_testimonial_author': data.get('client_testimonial_author'),
            }
        )
        if created:
            print(f"  Proyecto '{project.title}' creado.")
        else:
            print(f"  Proyecto '{project.title}' ya existe. Actualizando datos...")
            # Actualizar campos del proyecto si ya existía
            project.short_description = data['short_description']
            project.detailed_description = data['detailed_description']
            project.client = data.get('client')
            project.location = data.get('location')
            project.duration = data.get('duration')
            project.service_type = data.get('service_type')
            project.client_testimonial_quote = data.get('client_testimonial_quote')
            project.client_testimonial_author = data.get('client_testimonial_author')
            project.save()

        # Añadir categorías (ManyToMany)
        project_categories_to_add = [project_categories_map[cat_name] for cat_name in data['categories'] if cat_name in project_categories_map]
        project.categories.set(project_categories_to_add) # Siempre establece las relaciones
        print(f"    Categorías asociadas al proyecto '{project.title}'.")

        # Añadir servicios (ManyToMany)
        services_to_add = [service_map[svc_name] for svc_name in data['services_used'] if svc_name in service_map]
        project.services.set(services_to_add) # Siempre establece las relaciones
        print(f"    Servicios asociados al proyecto '{project.title}'.")

        # Añadir imágenes: borrar las existentes y crearlas de nuevo para asegurar que estén actualizadas
        # Esto es más simple que intentar comparar imágenes una por una
        ProjectImage.objects.filter(project=project).delete()
        for img_data in data['images']:
            ProjectImage.objects.create(
                project=project,
                image=ContentFile(DUMMY_IMAGE_DATA, name=img_data['name']),
                caption=img_data['caption'],
                is_main_image=img_data['is_main']
            )
            print(f"    Imagen '{img_data['name']}' para '{project.title}' creada.")

# --- Función principal para ejecutar el script ---
def run(*args, **kwargs):
    """
    Función principal para cargar los datos de ejemplo.
    Puede ser ejecutada con: python manage.py runscript seed_data
    """
    print("\n--- Iniciando la carga de datos de ejemplo para LE WORK Constructora ---")

    # --- Limpieza de datos existentes ---
    # ¡IMPORTANTE! Este bloque borra TODOS los datos de los modelos listados.
    # Úsalo con precaución, especialmente en entornos de producción.
    print("Limpiando datos existentes...")
    
    # El orden de borrado es crucial para evitar errores de clave foránea.
    # Se borra desde los modelos más dependientes a los menos dependientes.
    
    # 1. Modelos de Projects: Primero las imágenes, luego los proyectos, luego las categorías de proyecto.
    ProjectImage.objects.all().delete()
    Project.objects.all().delete()
    ProjectCategory.objects.all().delete()
    
    # 2. Modelos de Services: Primero los servicios, luego las categorías de servicio.
    Service.objects.all().delete()
    ServiceCategory.objects.all().delete()
    
    # 3. Modelos de About: Borra AboutUs (que tiene ManyToMany), luego testimonios, valores, y miembros del equipo.
    AboutUs.objects.all().delete() # Borra AboutUs antes de sus ManyToMany
    Testimonial.objects.all().delete()
    Value.objects.all().delete()
    TeamMember.objects.all().delete()
    
    # 4. Modelos de Core: ContactInfo (no tiene dependientes)
    ContactInfo.objects.all().delete()
    
    print("Limpieza completada.")
    # --- Fin de la limpieza ---

    # 1. Cargar información de contacto (es independiente)
    load_contact_info()

    # 2. Cargar datos de la app 'about' (el orden importa para AboutUs)
    team_members = load_team_members()
    values = load_values()
    testimonials = load_testimonials()
    load_about_us(team_members, values, testimonials)

    # 3. Cargar datos de la app 'services' (el orden importa para Service)
    service_categories = load_service_categories()
    services = load_services(service_categories)

    # 4. Cargar datos de la app 'projects' (el orden importa para ProjectImage)
    project_categories = load_project_categories()
    load_projects(project_categories, services)

    print("\n--- Carga de datos de ejemplo finalizada exitosamente. ---")