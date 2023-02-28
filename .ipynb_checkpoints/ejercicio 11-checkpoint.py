{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2c54ddf1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\n    3) Crea un DataFrame, de nombre df\\n\\n    con esa información en base a la siguiente relación de clientes y tarifas contratadas (€)\\n\\n    clientes: Ana Pérez, Juan García, Andrés Álvarez, Luis Ramos, Pedro Cadenas,\\n            Estefanía Miguélez, Alberto Delgado, Susana Castro, Luis González\\n\\n    tarifas: 40,50,50,35,45,50,60,50,45\\n'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"\n",
    "    Creado: Isabel Maniega\n",
    "    Fecha: 08/09/2022\n",
    "\"\"\"\n",
    "\n",
    "# Importar las librerías\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "# EJERCICIO 1\n",
    "\n",
    "\"\"\"\n",
    "    Escribe el código necesario en Python para:\n",
    "\n",
    "    almacenar con una lista de nombre \"clientes\" los siguientes nombres:\n",
    "\n",
    "    \"Ana Pérez\", \"Juan García\", \"Andres Álvarez\", \"Luis Ramos\", \"Pedro Cadenas\",\n",
    "    \"Estefanía Miguélez\", \"Alberto Delgado\", \"Susana Castro\", \"Luis González\"\n",
    "\"\"\"\n",
    "\n",
    "# 1) Para ese listado de clientes imprime todos ellos, 1 a 1\n",
    "\n",
    "\"\"\"\n",
    "    2) Dentro de ese grupo de clientes..\n",
    "\n",
    "    se pide buscar..al cliente de nombre: \"Juan García\" si es posible\n",
    "\n",
    "    Si lo encuentra, debería imprimir un mensaje tal que así:\n",
    "\n",
    "    \"el cliente -nombre del cliente- se encuentra en mi Base de Datos de Clientes\"\n",
    "\n",
    "    Si no se le encuentra, debería salir un mensaje tal que así:\n",
    "\n",
    "    \"el cliente -nombre del cliente- NO se encuentra en mi Base de Datos de Clientes\"\n",
    "\n",
    "    Nota: Comprueba en el caso de llevar o no acento\n",
    "\n",
    "    Para:\n",
    "\n",
    "    Juan García\n",
    "\n",
    "    Juan Garcia\n",
    "\n",
    "    Ojo con la tilde..\n",
    "\"\"\"\n",
    "\n",
    "\"\"\"\n",
    "    3) Crea un DataFrame, de nombre df\n",
    "\n",
    "    con esa información en base a la siguiente relación de clientes y tarifas contratadas (€)\n",
    "\n",
    "    clientes: Ana Pérez, Juan García, Andrés Álvarez, Luis Ramos, Pedro Cadenas,\n",
    "            Estefanía Miguélez, Alberto Delgado, Susana Castro, Luis González\n",
    "\n",
    "    tarifas: 40,50,50,35,45,50,60,50,45\n",
    "\"\"\"\n",
    "\n",
    "# 4) Imprime las primeras 5 filas del DataFrame de 2 formas distintas\n",
    "\n",
    "\n",
    "# 5) De ese DataFrame, selecciona solamente la columna \"tarifas\" e imprímela\n",
    "    # (con 1 forma es suficiente, pero si sabes 2 mejor)\n",
    "\n",
    "# 6) Descomenta las siguientes líneas (algunos trucos y cosas útiles).\n",
    "    # Ponlo en formato función!!\n",
    "\n",
    "# df.tarifas.value_counts()\n",
    "\n",
    "# df.tarifas.value_counts().plot(kind=\"bar\")\n",
    "# plt.show()\n",
    "\n",
    "# df.tarifas.plot(kind=\"bar\")\n",
    "# plt.show\n",
    "\n",
    "# print(df)\n",
    "\n",
    "\n",
    "# 7) De ese DataFrame, selecciona solamente aquellos clientes con tarifa superior a 50 euros (50 no incluído)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "031120e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9d721a02",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Ana Pérez',\n",
       " 'Juan García',\n",
       " 'Andres Álvarez',\n",
       " 'Luis Ramos',\n",
       " 'Pedro Cadenas',\n",
       " 'Estefanía Miguélez',\n",
       " 'Alberto Delgado',\n",
       " 'Susana Castro',\n",
       " 'Luis González']"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clientes = [\"Ana Pérez\", \"Juan García\", \"Andres Álvarez\", \"Luis Ramos\", \"Pedro Cadenas\",\n",
    "\"Estefanía Miguélez\", \"Alberto Delgado\", \"Susana Castro\", \"Luis González\"]\n",
    "clientes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fbf3d0f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ana Pérez\n",
      "Juan García\n",
      "Andres Álvarez\n",
      "Luis Ramos\n",
      "Pedro Cadenas\n",
      "Estefanía Miguélez\n",
      "Alberto Delgado\n",
      "Susana Castro\n",
      "Luis González\n"
     ]
    }
   ],
   "source": [
    "for cliente in clientes:\n",
    "    print(cliente)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "84b8fccd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Introduzca el nombre del cliente : Ana Pérez\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'El cliente Ana Pérez se encuentra en mi base de datos de Clientes'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nombre = input(\"Introduzca el nombre del cliente : \")\n",
    "def encontrar_cliente(nombre):\n",
    "    for cliente in clientes:\n",
    "        if cliente == nombre:\n",
    "            return f\"El cliente {nombre} se encuentra en mi base de datos de Clientes\"\n",
    "        else:\n",
    "            return f\"El cliente {nombre} NO se encuentra en mi Base de Datos de Clientes\"\n",
    "        \n",
    "    nombre = input(\"Introduzca el nombre del cliente: \")  \n",
    "encontrar_cliente(nombre)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "dfb93ff3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ana Pérez\n",
      "Juan García\n",
      "Andres Álvarez\n",
      "Luis Ramos\n",
      "Pedro Cadenas\n",
      "Estefanía Miguélez\n",
      "Alberto Delgado\n",
      "Susana Castro\n",
      "Luis González\n"
     ]
    }
   ],
   "source": [
    "def imprimir(lista):\n",
    "    try:\n",
    "        for cliente in lista:\n",
    "            print(cliente)\n",
    "    except Exception as e:\n",
    "        print(\"error en bucle for %s\" % str(e))\n",
    "imprimir(clientes)                 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0a6e40d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[40, 50, 50, 35, 45, 50, 60, 50, 45]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tarifas= [40,50,50,35,45,50,60,50,45]\n",
    "tarifas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "07eb77c3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Clientes</th>\n",
       "      <th>Tarifas</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Ana Pérez</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Juan García</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Andres Álvarez</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Luis Ramos</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Pedro Cadenas</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Estefanía Miguélez</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Alberto Delgado</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Susana Castro</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Luis González</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Clientes  Tarifas\n",
       "0           Ana Pérez       40\n",
       "1         Juan García       50\n",
       "2      Andres Álvarez       50\n",
       "3          Luis Ramos       35\n",
       "4       Pedro Cadenas       45\n",
       "5  Estefanía Miguélez       50\n",
       "6     Alberto Delgado       60\n",
       "7       Susana Castro       50\n",
       "8       Luis González       45"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame({\"Clientes\": clientes, \"Tarifas\": tarifas})\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a6b3a5db",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Clientes</th>\n",
       "      <th>Tarifas</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Ana Pérez</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Juan García</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Andres Álvarez</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Luis Ramos</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Pedro Cadenas</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Clientes  Tarifas\n",
       "0       Ana Pérez       40\n",
       "1     Juan García       50\n",
       "2  Andres Álvarez       50\n",
       "3      Luis Ramos       35\n",
       "4   Pedro Cadenas       45"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "8ae45584",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Clientes</th>\n",
       "      <th>Tarifas</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Pedro Cadenas</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Estefanía Miguélez</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Alberto Delgado</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Susana Castro</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Luis González</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Clientes  Tarifas\n",
       "4       Pedro Cadenas       45\n",
       "5  Estefanía Miguélez       50\n",
       "6     Alberto Delgado       60\n",
       "7       Susana Castro       50\n",
       "8       Luis González       45"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "ea72be1b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Clientes</th>\n",
       "      <th>Tarifas</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Ana Pérez</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Juan García</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Andres Álvarez</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Luis Ramos</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Pedro Cadenas</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Clientes  Tarifas\n",
       "0       Ana Pérez       40\n",
       "1     Juan García       50\n",
       "2  Andres Álvarez       50\n",
       "3      Luis Ramos       35\n",
       "4   Pedro Cadenas       45"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[0:5, 0:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "afdbf624",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    40\n",
       "1    50\n",
       "2    50\n",
       "3    35\n",
       "4    45\n",
       "5    50\n",
       "6    60\n",
       "7    50\n",
       "8    45\n",
       "Name: Tarifas, dtype: int64"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Tarifas\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e2b3a43",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "8a37b453",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50    4\n",
       "45    2\n",
       "40    1\n",
       "35    1\n",
       "60    1\n",
       "Name: Tarifas, dtype: int64"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Tarifas.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "fa796477",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.Tarifas.value_counts().plot(kind=\"bar\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "1a91c62f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function matplotlib.pyplot.show(close=None, block=None)>"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.Tarifas.plot(kind=\"bar\")\n",
    "plt.show"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "2b1a3d6a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Clientes</th>\n",
       "      <th>Tarifas</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Ana Pérez</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Juan García</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Andres Álvarez</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Luis Ramos</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Pedro Cadenas</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Estefanía Miguélez</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Alberto Delgado</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Susana Castro</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Luis González</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Clientes  Tarifas\n",
       "0           Ana Pérez       40\n",
       "1         Juan García       50\n",
       "2      Andres Álvarez       50\n",
       "3          Luis Ramos       35\n",
       "4       Pedro Cadenas       45\n",
       "5  Estefanía Miguélez       50\n",
       "6     Alberto Delgado       60\n",
       "7       Susana Castro       50\n",
       "8       Luis González       45"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d9cfc6a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "36d55fbe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\n    Intercambio de valores entre variables\\n\\n    Siendo por ejemplo:\\n\\n    x = 3 e y = 2\\n    Se pide hacer un pequeño algoritmo que me intercambie esos valores.\\n\\n    Y que sea el resultado:\\n\\n    x = 2 e y = 3\\n'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "\n",
    "# EJERCICIO 2\n",
    "\n",
    "# Número par o impar\n",
    "\n",
    "# Prueba para los números 6 y 3\n",
    "\n",
    "# Realiza un algortimo para saber si son pares o impares\n",
    "\n",
    "\n",
    "\n",
    "# EJERCICIO 3\n",
    "\n",
    "\"\"\"\n",
    "    Intercambio de valores entre variables\n",
    "\n",
    "    Siendo por ejemplo:\n",
    "\n",
    "    x = 3 e y = 2\n",
    "    Se pide hacer un pequeño algoritmo que me intercambie esos valores.\n",
    "\n",
    "    Y que sea el resultado:\n",
    "\n",
    "    x = 2 e y = 3\n",
    "\"\"\"\n",
    "\n",
    "# 1) Hazlo sin funciones\n",
    "\n",
    "# 2) Hazlo mismo con una función"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "40ee33ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Introduce un numero : 5\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'El numero 5 es un numero impar'"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numero = int(input(\"Introduce un numero : \"))\n",
    "def par_impar(numero):\n",
    "        if numero % 2 == 0:\n",
    "            return f\" El numero {numero} es un numero par\"\n",
    "      \n",
    "        else:          \n",
    "            return f\"El numero {numero} es un numero impar\"\n",
    "        \n",
    "par_impar(numero)        \n",
    "      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "e9ffdb4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 3\n",
    "y = 2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "ab79ff23",
   "metadata": {},
   "outputs": [],
   "source": [
    "x,y = y, x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "64c1eb96",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3)"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x,y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "3d540413",
   "metadata": {},
   "outputs": [],
   "source": [
    "temp = x\n",
    "x = y\n",
    "y = temp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "5221a299",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 2)"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x,y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "63871639",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "b9705be6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 5, 6],\n",
       "       [7, 8, 9]])"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "m3 =np.array([[1, 2, 3],\n",
    "                  [4, 5, 6],\n",
    "                  [7, 8, 9]])\n",
    "m3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "ab98de8b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "lista = []\n",
    "for x in range(len(matriz1)):\n",
    "    for y in range(len(matriz1[x])):\n",
    "        lista.append(matriz1[x][y])\n",
    "print(lista)\n",
    "matriz2 = np.array(lista)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "829903a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[1, 4, 7], [2, 5, 8], [3, 6, 9]]"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listi = []\n",
    "for i in range(len(m3)):\n",
    "    listi.append([])\n",
    "    for j in range(len(m3[i])):\n",
    "        listi[i].append(m3[j][i])\n",
    "listi    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "285639c7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 4, 7],\n",
       "       [2, 5, 8],\n",
       "       [3, 6, 9]])"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listo = np.array(listi)\n",
    "listo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bcdf0f34",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
