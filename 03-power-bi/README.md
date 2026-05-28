# Power BI — dashboard_lanas_excel

Esta carpeta contiene la integración Python con el archivo de datos de Power BI **dashboard_lanas_excel**.

## Estructura

```
03-power-bi/
├── connector.py               # Módulo principal de conexión al Excel
├── create_sample_data.py      # Genera dashboard_lanas_excel.xlsx de ejemplo
├── dashboard_lanas_excel.xlsx # Archivo de datos (generado por create_sample_data.py)
└── README.md                  # Esta guía
```

## Descripción del dashboard

El dashboard **dashboard_lanas_excel** contiene datos de un negocio de venta de lanas:

| Hoja          | Descripción                                      |
|---------------|--------------------------------------------------|
| `Ventas`      | Registro de ventas con fecha, producto y totales |
| `Inventario`  | Stock actual por producto y color                |
| `Proveedores` | Información de proveedores y plazos de entrega   |

## Uso rápido

### 1. Generar el archivo Excel de ejemplo

```bash
uv run python 03-power-bi/create_sample_data.py
```

Esto crea `03-power-bi/dashboard_lanas_excel.xlsx` con datos de ejemplo.

### 2. Conectarse y leer los datos en Python

```python
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "03-power-bi"))
from connector import connect, summary

data = connect()          # LanasData(ventas=..., inventario=..., proveedores=...)
print(data.ventas.head())
print(summary(data))
```

### 3. Ejecutar el script de demostración

```bash
# Primero genera el Excel si aún no existe:
uv run python 03-power-bi/create_sample_data.py

# Luego corre el conector:
uv run python 03-power-bi/connector.py
```

## API del conector

### `connect(excel_path=None) → LanasData`

Abre el archivo Excel y devuelve un `NamedTuple` con tres DataFrames:

| Atributo      | Tipo             | Contenido                   |
|---------------|------------------|-----------------------------|
| `ventas`      | `pd.DataFrame`   | Hoja *Ventas*               |
| `inventario`  | `pd.DataFrame`   | Hoja *Inventario*           |
| `proveedores` | `pd.DataFrame`   | Hoja *Proveedores*          |

**Parámetros:**

- `excel_path` *(str | Path | None)*: ruta al archivo `.xlsx`.  
  Cuando es `None` se usa `03-power-bi/dashboard_lanas_excel.xlsx`.

**Excepciones:**

- `FileNotFoundError`: si el archivo no existe en la ruta indicada.

### `summary(data) → dict`

Devuelve un diccionario con métricas de alto nivel:

```json
{
  "total_ventas": 102250.0,
  "ventas_por_producto": { "Alpaca Premium": 25200.0, ... },
  "productos_en_inventario": 4,
  "valor_total_inventario": 157860.0,
  "stock_total_unidades": 413,
  "proveedores": 4
}
```

## Dependencias

Las dependencias se agregan automáticamente al instalar el entorno del proyecto:

```bash
make install   # instala pandas y openpyxl junto con el resto
```

Los paquetes requeridos son `pandas>=2.0.0` y `openpyxl>=3.1.0`.

## Integración con Power BI

Para usar estos datos en Power BI Desktop:

1. Abre Power BI Desktop.
2. **Inicio → Obtener datos → Excel**.
3. Selecciona `dashboard_lanas_excel.xlsx`.
4. Activa las hojas **Ventas**, **Inventario** y **Proveedores**.
5. Haz clic en **Cargar**.

El conector Python es útil para preprocesar, validar o enriquecer los datos con IA antes de actualizarlos en el Excel que consume Power BI.
