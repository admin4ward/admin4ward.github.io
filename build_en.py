#!/usr/bin/env python3
"""Genera en.html (versión en inglés) a partir de index.html.
Uso: python3 build_en.py   (junto a index.html)
Cada texto visible en español debe tener su traducción en T; el script avisa de lo que falte."""
import re, sys, pathlib
aqui = pathlib.Path(__file__).resolve().parent
raiz = aqui if (aqui / 'index.html').exists() else aqui.parent
s = (raiz / 'index.html').read_text(encoding='utf8')

# Bloques que solo existen en español (redirección y aviso de idioma)
s = re.sub(r'<!--ES-ONLY-->.*?<!--/ES-ONLY-->\n?', '', s, flags=re.S)

# Estructura y enlaces
E = [
 ('<html lang="es">', '<html lang="en">'),
 ('<link rel="canonical" href="https://admin4ward.github.io/">', '<link rel="canonical" href="https://admin4ward.github.io/en">'),
 ('<title>FOURWARD · Consultoría, formación e IA aplicada</title>', '<title>FOURWARD · Consulting, training and applied AI</title>'),
 ('content="FOURWARD: estrategia, tecnología y formación para que tu organización convierta lo que sabe en decisiones y resultados. Bogotá, Colombia."',
  'content="FOURWARD: strategy, technology and training that help your organization turn what it knows into decisions and results. Bogotá, Colombia."'),
 ('content="FOURWARD · Avanza con inteligencia"', 'content="FOURWARD · Consulting, training and applied AI"'),
 ('content="Consultoría empresarial, tecnología aplicada y formación corporativa."', 'content="Business consulting, applied technology and corporate training."'),
 ('href="en" hreflang="en" lang="en" data-idioma="en" aria-label="English version" title="English version">EN</a>',
  'href="./" hreflang="es" lang="es" data-idioma="es" aria-label="Versión en español" title="Versión en español">ES</a>'),
 ("' de ' + PREGUNTAS.length", "' of ' + PREGUNTAS.length"),
 ("' de 10'", "' of 10'"), ("' de 10 ('", "' of 10 ('"),
]
for a, b in E:
    n = s.count(a)
    if n < 1: sys.exit('No encontrado: ' + a)
    s = s.replace(a, b)

T = {
# --- Menú y portada ---
'Saltar al contenido': 'Skip to content',
'FOURWARD, inicio': 'FOURWARD, home',
'Abrir menú': 'Open menu', 'Cerrar menú': 'Close menu',
'Pie de página': 'Footer',
'Cómo trabajamos contigo': 'How we work with you',
'Cómo trabajamos': 'How we work',
'Acceso equipo · 4Ward Opera': 'Team access · 4Ward Opera',
'Acceso equipo': 'Team access',
'Hablemos de tu próximo desafío': 'Let’s talk about your next challenge',
'Hablemos de tu desafío': 'Tell us about your challenge',
'Consultoría · Formación · IA aplicada': 'Consulting · Training · Applied AI',
'Conocimiento que impulsa': 'Knowledge that drives',
'crecimiento.': 'growth.',
'Estrategia, tecnología y formación para que tu organización convierta lo que sabe en decisiones y resultados.':
  'Strategy, technology and training that help your organization turn what it knows into decisions and results.',
'Conoce nuestras soluciones': 'Explore our solutions',
'Nuestras tres capacidades': 'Our three capabilities',
'Dirección clara y decisiones con criterio: convertimos un desafío en un plan de acción.':
  'Clear direction and sound decisions: we turn a challenge into an action plan.',
'Inteligencia artificial, automatización y datos elegidos por su utilidad para el negocio.':
  'Artificial intelligence, automation and data, chosen for what they do for the business.',
'Formación aplicada para que las capacidades del equipo se conviertan en acción.':
  'Applied training that turns your team’s capabilities into action.',
# --- Contexto ---
'El contexto': 'The context',
'El mundo empresarial cambia. La manera de avanzar también.': 'Business is changing. So is the way forward.',
'Las organizaciones necesitan responder con inteligencia a desafíos cada vez más complejos.':
  'Organizations need to respond intelligently to increasingly complex challenges.',
'Nuestra convicción': 'What we believe',
'Hoy no basta con tener información. Hay que convertirla en decisiones y acción.':
  'Having information is no longer enough. It has to become decisions and action.',
'Competitividad': 'Competitiveness',
'Mercados dinámicos y decisiones que requieren mayor claridad.': 'Fast-moving markets and decisions that call for more clarity.',
'Productividad y mejora de procesos': 'Productivity and process improvement',
'Productividad': 'Productivity',
'Procesos que necesitan evolucionar y aprovechar mejor sus recursos.': 'Processes that need to evolve and make better use of resources.',
'Transformación digital': 'Digital transformation',
'Tecnologías que abren oportunidades, pero exigen adaptación.': 'Technologies that open opportunities but demand adaptation.',
'Capacidades del equipo': 'Team capabilities',
'Conocimiento y habilidades que deben actualizarse constantemente.': 'Knowledge and skills that need constant updating.',
# --- Explorador ---
'¿Qué necesitas lograr?': 'What do you need to achieve?',
'El punto de partida es tu desafío. Elige el que más se parece al tuyo y mira cómo lo abordamos.':
  'We start from your challenge. Pick the one closest to yours and see how we approach it.',
'¿No tienes claro por dónde empezar?': 'Not sure where to start?',
'Haz el diagnóstico rápido': 'Take the quick assessment',
': cinco preguntas, dos minutos.': ': five questions, two minutes.',
'Necesidades': 'Needs',
'Fortalecer equipos': 'Strengthen teams',
'Tu equipo necesita nuevas capacidades.': 'Your team needs new capabilities.',
'Diseñamos experiencias de aprendizaje a partir de lo que el equipo debe lograr en su trabajo, no de un temario genérico.':
  'We design learning experiences around what the team has to achieve at work, not around a generic syllabus.',
'Cotizar una formación': 'Request a training quote',
'Cursos y talleres prácticos': 'Hands-on courses and workshops',
'Herramientas, ejercicios y situaciones reales de negocio.': 'Tools, exercises and real business situations.',
'Masterclass y conferencias': 'Masterclasses and talks',
'Actualización ejecutiva en un tema prioritario.': 'An executive update on a priority topic.',
'Programas de formación corporativa': 'Corporate training programs',
'Rutas de aprendizaje en varios encuentros o módulos.': 'Learning paths across several sessions or modules.',
'Capacitación a la medida': 'Tailored training',
'Contenidos y metodología ajustados a tu contexto.': 'Content and methodology adapted to your context.',
'Resolver un reto organizacional': 'Solve an organizational challenge',
'Hay un problema que frena a la organización.': 'A problem is holding the organization back.',
'Empezamos por entender el negocio. Con el diagnóstico definimos prioridades y un plan de acción que se pueda ejecutar.':
  'We start by understanding the business. The diagnosis lets us set priorities and an action plan that can actually be carried out.',
'Conversar sobre el reto': 'Discuss the challenge',
'Diagnóstico y análisis empresarial': 'Business diagnosis and analysis',
'Lectura del contexto, brechas y oportunidades priorizadas.': 'A reading of the context, gaps and prioritized opportunities.',
'Planeación estratégica': 'Strategic planning',
'Objetivos, decisiones clave y rutas de trabajo.': 'Objectives, key decisions and roadmaps.',
'Mejora de procesos': 'Process improvement',
'Revisión y optimización de la operación.': 'Reviewing and optimizing operations.',
'Indicadores y seguimiento de resultados': 'Metrics and results tracking',
'Indicadores y seguimiento': 'Metrics and tracking',
'Métricas para orientar decisiones y medir el avance.': 'Metrics to guide decisions and measure progress.',
'Explorar oportunidades tecnológicas': 'Explore technology opportunities',
'Quieres aprovechar la IA y la automatización con criterio.': 'You want to use AI and automation wisely.',
'Identificamos dónde la tecnología aporta valor real, priorizamos los casos de uso y acompañamos su adopción.':
  'We identify where technology adds real value, prioritize the use cases and support their adoption.',
'Explorar oportunidades': 'Explore opportunities',
'Inteligencia artificial aplicada al negocio': 'AI applied to the business',
'Inteligencia artificial aplicada': 'Applied artificial intelligence',
'Casos de uso prácticos para el trabajo de tu empresa.': 'Practical use cases for the work your company does.',
'Tareas y flujos que se pueden simplificar.': 'Tasks and workflows that can be simplified.',
'Digitalización y optimización de procesos': 'Process digitalization and optimization',
'Digitalización de procesos': 'Process digitalization',
'Herramientas para mejorar la operación y la colaboración.': 'Tools to improve operations and collaboration.',
'Uso estratégico de datos e información': 'Strategic use of data and information',
'Uso estratégico de datos': 'Strategic use of data',
'Información convertida en apoyo para decidir.': 'Information turned into support for decisions.',
'Desarrollar una iniciativa': 'Develop an initiative',
'Tienes un proyecto y necesitas estructurarlo.': 'You have a project and need to structure it.',
'Te ayudamos a pasar de la idea a un proyecto con alcance claro, responsables y resultados que se puedan verificar.':
  'We help you move from an idea to a project with a clear scope, owners and results that can be verified.',
'Estructurar mi iniciativa': 'Structure my initiative',
'Definición de objetivos, decisiones clave y rutas de trabajo.': 'Defining objectives, key decisions and roadmaps.',
'Definición de objetivos': 'Defining objectives',
'Qué significa avanzar y cómo se va a medir.': 'What progress means and how it will be measured.',
'Alcance y metodología': 'Scope and methodology',
'Qué se hará, qué no, y en qué fases.': 'What will be done, what will not, and in which phases.',
'Productos de trabajo con criterio de aceptación.': 'Work products with acceptance criteria.',
'Gestión y acompañamiento': 'Management and support',
'Coordinación, seguimiento y puntos de control.': 'Coordination, follow-up and checkpoints.',
'Agendar una conversación': 'Schedule a conversation',
'Otro tema': 'Something else',
# --- Soluciones ---
'Nuestras soluciones': 'Our solutions',
'Servicios para desafíos reales.': 'Services for real challenges.',
'Tres líneas de servicio que pueden integrarse o desarrollarse de manera independiente.':
  'Three service lines that can be combined or delivered on their own.',
'Consultoría empresarial': 'Business consulting',
'Diagnóstico, dirección y ejecución': 'Diagnosis, direction and execution',
'Acompañamiento para comprender desafíos, estructurar estrategias y activar iniciativas de mejora.':
  'Support to understand challenges, structure strategies and launch improvement initiatives.',
'Para empresas que necesitan convertir un desafío en un plan de acción.': 'For companies that need to turn a challenge into an action plan.',
'Lectura del contexto, identificación de brechas y priorización de oportunidades.':
  'Reading the context, identifying gaps and prioritizing opportunities.',
'Planeación y estructuración estratégica': 'Strategic planning and structuring',
'Revisión de procesos e identificación de oportunidades de optimización.': 'Reviewing processes and identifying optimization opportunities.',
'Gestión de proyectos e iniciativas': 'Project and initiative management',
'Estructuración, acompañamiento y coordinación de proyectos.': 'Structuring, supporting and coordinating projects.',
'Diseño y lectura de métricas para orientar decisiones y mejoras.': 'Designing and reading metrics to guide decisions and improvements.',
'Tecnología e innovación aplicada': 'Applied technology and innovation',
'Herramientas con sentido empresarial': 'Tools that make business sense',
'Herramientas tecnológicas seleccionadas por su utilidad para los procesos y objetivos del negocio.':
  'Technology tools selected for what they contribute to business processes and goals.',
'Identificar el potencial. Priorizar su valor. Acompañar la adopción.': 'Identify the potential. Prioritize its value. Support adoption.',
'Identificación de casos de uso y oportunidades prácticas para el trabajo empresarial.':
  'Identifying use cases and practical opportunities for business work.',
'Oportunidades de automatización': 'Automation opportunities',
'Exploración de tareas y flujos susceptibles de simplificación.': 'Exploring tasks and workflows that can be simplified.',
'Análisis de herramientas para mejorar la operación y la colaboración.': 'Assessing tools to improve operations and collaboration.',
'Enfoques para interpretar información y apoyar decisiones.': 'Approaches to interpret information and support decisions.',
'Adopción de nuevas herramientas': 'Adopting new tools',
'Acompañamiento para integrar nuevas formas de trabajar.': 'Support to bring new ways of working into the organization.',
'Formación empresarial': 'Corporate training',
'Conocimiento que se pone en práctica': 'Knowledge put into practice',
'Experiencias de aprendizaje para fortalecer habilidades y capacidades relevantes para cada organización.':
  'Learning experiences that build the skills and capabilities each organization needs.',
'Cada programa define objetivos, público, temas y entregables específicos.':
  'Each program sets its own objectives, audience, topics and deliverables.',
'Conferencias empresariales': 'Business talks',
'Sesiones de inspiración, actualización y reflexión aplicada.': 'Sessions for inspiration, updates and applied reflection.',
'Masterclass especializadas': 'Specialized masterclasses',
'Profundización ejecutiva en un tema prioritario.': 'An executive deep dive into a priority topic.',
'Aprendizaje orientado a herramientas, ejercicios y situaciones de negocio.': 'Learning built around tools, exercises and business situations.',
'Rutas de aprendizaje articuladas en varios encuentros o módulos.': 'Learning paths structured across several sessions or modules.',
'Contenidos y metodología ajustados al contexto del cliente.': 'Content and methodology adapted to the client’s context.',
# --- Formación ---
'Aprender, aplicar y transformar.': 'Learn, apply and transform.',
'Una propuesta de formación responde a una necesidad concreta del negocio, no solo a un temario. Así se vive cada programa.':
  'A training proposal answers a specific business need, not just a syllabus. This is how each program unfolds.',
'Contexto y conceptos clave': 'Context and key concepts',
'Partimos de la realidad del equipo para dar criterio y tomar mejores decisiones.':
  'We start from the team’s reality to build judgment and better decisions.',
'Herramientas y ejercicios': 'Tools and exercises',
'Casos, demostraciones y dinámicas relacionadas con el trabajo de cada día.': 'Cases, demonstrations and activities tied to everyday work.',
'Aplicación al trabajo': 'Application at work',
'Prácticas que se pueden trasladar a la operación al terminar la sesión.': 'Practices that can be taken into operations as soon as the session ends.',
'Temas en los que formamos': 'Topics we teach',
'Los temas y su profundidad se ajustan al alcance de cada programa.': 'Topics and depth are adjusted to the scope of each program.',
'Excel para análisis de datos': 'Excel for data analysis',
'Fundamentos de Machine Learning': 'Machine Learning fundamentals',
# --- Método ---
'Nuestra forma de trabajar': 'Our way of working',
'Del entendimiento a la acción.': 'From understanding to action.',
'Partimos del contexto del cliente para construir intervenciones relevantes y aplicables.':
  'We start from the client’s context to build relevant, applicable work.',
'Escuchamos al cliente, reconocemos sus necesidades y analizamos el contexto del negocio.':
  'We listen to the client, recognize their needs and analyze the business context.',
'Una lectura clara de tu situación y de las oportunidades prioritarias.': 'A clear reading of your situation and the priority opportunities.',
'Estructuramos una propuesta alineada con objetivos, capacidades y prioridades.':
  'We structure a proposal aligned with objectives, capabilities and priorities.',
'Una propuesta con objetivos, alcance, entregables e inversión.': 'A proposal with objectives, scope, deliverables and investment.',
'Desarrollamos las actividades acordadas y promovemos la aplicación práctica.':
  'We carry out the agreed activities and promote practical application.',
'Las actividades ejecutadas hombro a hombro con tu equipo.': 'The activities delivered side by side with your team.',
'Revisamos avances y oportunidades de mejora según el alcance definido.':
  'We review progress and improvement opportunities against the agreed scope.',
'Un balance de avances y recomendaciones para continuar.': 'A summary of progress and recommendations for what comes next.',
'Lo que puedes esperar de nosotros': 'What you can expect from us',
'Alcance claro desde el inicio': 'Clear scope from the start',
'Antes de empezar acordamos objetivos, entregables e inversión en una propuesta a tu medida.':
  'Before we begin, we agree on objectives, deliverables and investment in a proposal tailored to you.',
'Trabajo hombro a hombro': 'Side-by-side work',
'Construimos las soluciones con las personas que las van a usar, no a espaldas de la operación.':
  'We build solutions with the people who will use them, never behind the back of operations.',
'Capacidad que se queda': 'Capability that stays',
'Cada intervención busca que tu equipo pueda sostener y continuar lo logrado.':
  'Every engagement aims for your team to sustain and build on what was achieved.',
'Soluciones relevantes, ejecución organizada y aprendizaje aplicado.': 'Relevant solutions, organized execution and applied learning.',
# --- Diagnóstico ---
'Diagnóstico rápido': 'Quick assessment',
'¿Qué tan lista está tu organización para avanzar?': 'How ready is your organization to move forward?',
'Responde cinco afirmaciones sobre tu empresa y recibe una lectura inicial de dónde conviene empezar.':
  'Answer five statements about your company and get a first reading of where to start.',
'Es una orientación, no reemplaza un diagnóstico empresarial. Tus respuestas no se guardan ni se envían: se calculan en tu navegador.':
  'This is guidance, not a substitute for a business diagnosis. Your answers are not stored or sent: they are calculated in your browser.',
'Ver mi resultado': 'See my result',
'Las prioridades del año están definidas y el equipo las conoce.': 'This year’s priorities are defined and the team knows them.',
'Los procesos clave están documentados y se mejoran con regularidad.': 'Key processes are documented and improved regularly.',
'Tomamos decisiones con indicadores confiables y actualizados.': 'We make decisions with reliable, up-to-date metrics.',
'Usamos automatización o inteligencia artificial en tareas del día a día.': 'We use automation or artificial intelligence in day-to-day tasks.',
'El equipo recibe formación en las habilidades que el negocio necesita.': 'The team is trained in the skills the business needs.',
'Todavía no': 'Not yet', 'En parte': 'Partly', 'Sí, de forma estable': 'Yes, consistently',
'Conviene empezar por ordenar prioridades y procesos: un diagnóstico y un plan de acción dan la base para todo lo demás.':
  'It makes sense to start by putting priorities and processes in order: a diagnosis and an action plan lay the groundwork for everything else.',
'Hay espacio para aprovechar mejor los datos y la tecnología: identificar casos de uso concretos es un buen primer paso.':
  'There is room to get more from data and technology: identifying specific use cases is a good first step.',
'El mayor avance puede venir de las capacidades del equipo: una formación a la medida acelera lo demás.':
  'The biggest gain may come from team capabilities: tailored training speeds up everything else.',
'Punto de partida': 'Starting point',
'Hay bases por construir. Es un buen momento para definir prioridades antes de invertir en herramientas.':
  'There are foundations still to build. It is a good moment to define priorities before investing in tools.',
'En desarrollo': 'Developing',
'Tienes avances reales y algunas brechas. Enfocar el esfuerzo en una o dos de ellas suele rendir más que abarcarlo todo.':
  'You have real progress and some gaps. Focusing on one or two of them usually pays off more than tackling everything.',
'Consolidado': 'Established',
'La organización tiene bases sólidas. El reto ahora es sostenerlas y buscar el siguiente nivel de madurez.':
  'The organization has solid foundations. The challenge now is to sustain them and reach the next level of maturity.',
'Falta responder: ': 'Still to answer: ',
'Tu resultado: ': 'Your result: ',
'No aparece una brecha evidente. Una conversación puede ayudar a identificar el siguiente reto.':
  'No obvious gap shows up. A conversation can help identify the next challenge.',
'Por dónde empezar: ': 'Where to start: ',
'Conversar sobre este resultado': 'Discuss this result',
'Hice el diagnóstico rápido del sitio. Resultado: ': 'I took the quick assessment on your site. Result: ',
'\\n\\nMe gustaría conversar sobre ': '\\n\\nI would like to talk about ',
'Responder de nuevo': 'Start over',
# --- Perspectivas ---
'Ideas para decidir mejor.': 'Ideas for better decisions.',
'Puntos de vista de nuestro equipo sobre estrategia, tecnología y conocimiento en las organizaciones.':
  'Our team’s points of view on strategy, technology and knowledge in organizations.',
'Inteligencia artificial': 'Artificial intelligence',
'Antes de elegir una herramienta de IA, elige el problema.': 'Before you choose an AI tool, choose the problem.',
'Muchas iniciativas de IA empiezan por la tecnología y terminan buscando para qué usarla. El orden contrario da mejores resultados.':
  'Many AI initiatives start with the technology and end up looking for something to use it on. The opposite order works better.',
'Leer la perspectiva': 'Read the perspective',
'La pregunta útil no es qué puede hacer la inteligencia artificial, sino qué tarea de tu operación consume tiempo, se repite y tiene un resultado que se puede verificar. Ahí suele estar el primer caso de uso.':
  'The useful question is which task in your operation takes time, repeats itself and has a result you can verify, rather than what artificial intelligence can do. That is usually where the first use case is.',
'Un buen primer caso es pequeño, tiene un responsable y se puede medir en semanas. Sirve para aprender cómo reacciona el equipo, qué datos hacen falta y qué controles se necesitan antes de ampliar el alcance.':
  'A good first case is small, has an owner and can be measured within weeks. It teaches you how the team reacts, what data is missing and what controls are needed before widening the scope.',
'Empieza por un proceso concreto, define cómo sabrás que mejoró y solo entonces elige la herramienta.':
  'Start with a specific process, define how you will know it improved, and only then choose the tool.',
'Datos y decisiones': 'Data and decisions',
'Un indicador que nadie consulta no orienta ninguna decisión.': 'A metric nobody looks at guides no decision.',
'Los tableros se multiplican con facilidad. Lo difícil es que cada cifra tenga un dueño y una decisión asociada.':
  'Dashboards multiply easily. The hard part is giving every figure an owner and a decision it informs.',
'Medir cuesta: alguien captura el dato, alguien lo consolida y alguien lo presenta. Ese esfuerzo solo se justifica cuando el indicador cambia lo que hace la organización.':
  'Measuring has a cost: someone captures the data, someone consolidates it and someone presents it. That effort is only justified when the metric changes what the organization does.',
'Una prueba sencilla es preguntar, para cada indicador, quién lo revisa, cada cuánto y qué haría distinto si mañana empeorara. Si no hay respuesta, el indicador sobra o está mal definido.':
  'A simple test is to ask, for each metric, who reviews it, how often, and what they would do differently if it got worse tomorrow. If there is no answer, the metric is unnecessary or poorly defined.',
'Pocos indicadores, con responsable y con una decisión detrás, valen más que un tablero completo.':
  'A few metrics, each with an owner and a decision behind it, are worth more than a full dashboard.',
'Una capacitación termina. Una capacidad se queda.': 'A training session ends. A capability stays.',
'Asistir a un curso no garantiza que el trabajo cambie. La diferencia está en lo que ocurre después de la sesión.':
  'Attending a course does not guarantee that work will change. The difference lies in what happens after the session.',
'La formación produce resultados cuando parte de una necesidad del negocio y no de un catálogo de temas. Eso define a quién formar, en qué y con qué ejemplos.':
  'Training delivers results when it starts from a business need and not from a catalog of topics. That defines who to train, in what, and with which examples.',
'También ayuda practicar con casos propios y acordar, antes de terminar, qué va a aplicar cada persona en su trabajo y quién le hará seguimiento.':
  'It also helps to practice with your own cases and to agree, before finishing, what each person will apply in their work and who will follow up.',
'Diseña la formación a partir de lo que el equipo debe lograr y planea la aplicación desde el primer día.':
  'Design training around what the team must achieve, and plan its application from day one.',
# --- Nosotros ---
'Quiénes somos': 'Who we are',
'Somos FOURWARD. Impulsamos organizaciones que quieren avanzar.': 'We are FOURWARD. We drive organizations that want to move forward.',
'Consultoría y formación empresarial con una visión integral de estrategia, tecnología y conocimiento. Acompañamos a las organizaciones a comprender sus retos, identificar oportunidades, desarrollar capacidades y construir caminos de evolución.':
  'Business consulting and training with an integrated view of strategy, technology and knowledge. We help organizations understand their challenges, identify opportunities, develop capabilities and build paths to evolve.',
'Nuestro propósito: impulsar organizaciones que aprenden, aplican y crecen.': 'Our purpose: to drive organizations that learn, apply and grow.',
'Para cada proyecto conformamos el equipo de especialistas según el alcance y la necesidad del cliente.':
  'For each project we assemble the team of specialists that fits the scope and the client’s need.',
'Nuestra forma de pensar': 'How we think',
'Conocemos el contexto antes de recomendar soluciones.': 'We learn the context before recommending solutions.',
'Integramos negocio, tecnología y personas.': 'We bring business, technology and people together.',
'Promovemos la aplicación práctica del conocimiento.': 'We promote the practical application of knowledge.',
'Red de expertos FOURWARD': 'FOURWARD expert network',
'Red de expertos': 'Expert network',
'¿Eres especialista en tu campo? Trabajemos juntos.': 'Are you a specialist in your field? Let’s work together.',
'Conformamos el equipo de cada proyecto según su alcance. Si tienes experiencia en consultoría, tecnología o formación empresarial, cuéntanos en qué podrías aportar.':
  'We assemble each project team according to its scope. If you have experience in consulting, technology or corporate training, tell us where you could contribute.',
'Quiero sumarme': 'I want to join',
'Nombre:\\nÁrea de experiencia:\\nPerfil o LinkedIn:\\n\\nCómo podría aportar:\\n': 'Name:\\nArea of expertise:\\nProfile or LinkedIn:\\n\\nHow I could contribute:\\n',
# --- Contacto ---
'Construyamos el siguiente paso': 'Let’s build the next step',
'Las organizaciones que avanzan convierten el conocimiento en acción.': 'Organizations that move forward turn knowledge into action.',
'Cuéntanos tu desafío. El alcance y la inversión se precisan en una propuesta comercial personalizada.':
  'Tell us about your challenge. Scope and investment are set out in a tailored commercial proposal.',
'Agendar una reunión': 'Book a meeting',
'Escribe tu nombre.': 'Enter your name.',
'Escribe un correo válido, por ejemplo nombre@empresa.com.': 'Enter a valid email, for example name@company.com.',
'Cuéntanos un poco más': 'Tell us a bit more',
'Cuéntanos en una o dos líneas qué necesitas.': 'Tell us in a line or two what you need.',
'Preparar mensaje': 'Prepare message',
'Selecciona y copia': 'Select and copy',
'Abrir en mi correo': 'Open in my email',
'Copiar mensaje': 'Copy message',
'Escribir otro mensaje': 'Write another message',
'Contacto web: ': 'Website contact: ',
'Nombre: ': 'Name: ', 'Empresa: ': 'Company: ', 'Correo: ': 'Email: ',
'\\nNecesidad: ': '\\nNeed: ',
'Recibimos tu mensaje': 'We received your message',
'Gracias, ': 'Thank you, ',
'. Te responderemos al correo ': '. We will reply to ',
'No pudimos enviarlo desde aquí': 'We could not send it from here',
'Tu mensaje no se perdió. Envíalo desde tu correo a ': 'Your message was not lost. Send it from your email to ',
'Tu mensaje está listo': 'Your message is ready',
'Ábrelo en tu correo para enviarlo a ': 'Open it in your email to send it to ',
', o cópialo y pégalo donde prefieras.': ', or copy and paste it wherever you prefer.',
'Estrategia · Tecnología · Conocimiento': 'Strategy · Technology · Knowledge',
}
# Palabras sueltas: solo como palabra completa
W = {
'Soluciones': 'Solutions', 'Formación': 'Training', 'Perspectivas': 'Insights', 'Nosotros': 'About us', 'Hablemos': 'Let’s talk',
'Estrategia': 'Strategy', 'Tecnología': 'Technology', 'Conocimiento': 'Knowledge',
'Explorar': 'Explore', 'Practicar': 'Practice', 'Transferir': 'Transfer',
'Modalidad': 'Format', 'Presencial': 'In person', 'Virtual': 'Online', 'Híbrida': 'Hybrid',
'Entendemos': 'We understand', 'Diseñamos': 'We design', 'Implementamos': 'We implement', 'Evaluamos': 'We evaluate',
'Recibes': 'You get', 'Entender': 'Understand', 'Conectar': 'Connect', 'Activar': 'Activate',
'Correo': 'Email', 'Copiar': 'Copy', 'Copiado': 'Copied', 'Ubicación': 'Location', 'Nombre': 'Name', 'Empresa': 'Company',
'Diagnóstico': 'Assessment', 'Contacto': 'Contact', 'Procesos': 'Processes', 'Datos': 'Data', 'Personas': 'People',
'Entregables': 'Deliverables', 'Automatización': 'Automation', 'Principal': 'Main',
}
# Solo se traduce el documento visible y los scripts, no las hojas de estilo
corte = s.index('</style>\n</head>')
cab, cuerpo = s[:corte], s[corte:]
for es in sorted(T, key=len, reverse=True):
    en = T[es]
    if es not in cuerpo: print('aviso: ya no está en la página ->', es[:70]); continue
    # dentro de los scripts los textos van entre comillas simples: se usa el apóstrofo tipográfico
    cuerpo = cuerpo.replace(es, en)
L = r'A-Za-zÁÉÍÓÚáéíóúñÑ_\-'
for es, en in W.items():
    cuerpo = re.sub(r'(?<![%s#.$/])%s(?![%s])' % (L, re.escape(es), L), en, cuerpo)
s = cab + cuerpo
(raiz / 'en.html').write_text(s, encoding='utf8')
print('en.html listo:', len(s), 'bytes')
