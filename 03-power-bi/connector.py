"""
connector.py — Python connector for the dashboard_lanas_excel Power BI data source.

Reads the three sheets of the Excel workbook and exposes them as pandas DataFrames
so that any Python script (or notebook) can work with the same data that feeds the
Power BI report.
"""

from __future__ import annotations

from pathlib import Path
from typing import NamedTuple

import pandas as pd


# Default path: the .xlsx file lives in the same directory as this module.
DEFAULT_EXCEL_PATH = Path(__file__).parent / "dashboard_lanas_excel.xlsx"

SHEET_VENTAS = "Ventas"
SHEET_INVENTARIO = "Inventario"
SHEET_PROVEEDORES = "Proveedores"


class LanasData(NamedTuple):
    """Container for all sheets loaded from dashboard_lanas_excel.xlsx."""

    ventas: pd.DataFrame
    inventario: pd.DataFrame
    proveedores: pd.DataFrame


def connect(excel_path: str | Path | None = None) -> LanasData:
    """
    Open *dashboard_lanas_excel.xlsx* and return all sheets as DataFrames.

    Args:
        excel_path: Path to the Excel file.  When *None* the file is looked up
                    next to this module (``03-power-bi/dashboard_lanas_excel.xlsx``).

    Returns:
        :class:`LanasData` named-tuple with attributes *ventas*, *inventario*,
        and *proveedores*.

    Raises:
        FileNotFoundError: if the Excel file does not exist at the given path.
    """
    path = Path(excel_path) if excel_path is not None else DEFAULT_EXCEL_PATH

    if not path.exists():
        raise FileNotFoundError(
            f"Excel file not found: {path}\n"
            "Run 'python 03-power-bi/create_sample_data.py' to generate it."
        )

    ventas = pd.read_excel(path, sheet_name=SHEET_VENTAS, parse_dates=["Fecha"])
    inventario = pd.read_excel(path, sheet_name=SHEET_INVENTARIO)
    proveedores = pd.read_excel(path, sheet_name=SHEET_PROVEEDORES)

    return LanasData(ventas=ventas, inventario=inventario, proveedores=proveedores)


def summary(data: LanasData) -> dict:
    """
    Return a high-level summary of the loaded data.

    Args:
        data: :class:`LanasData` as returned by :func:`connect`.

    Returns:
        Dictionary with key metrics extracted from the three sheets.
    """
    ventas = data.ventas
    inventario = data.inventario

    return {
        "total_ventas": float(ventas["Total"].sum()),
        "ventas_por_producto": ventas.groupby("Producto")["Total"].sum().to_dict(),
        "productos_en_inventario": int(inventario["Producto"].nunique()),
        "valor_total_inventario": float(inventario["Valor_Total"].sum()),
        "stock_total_unidades": int(inventario["Stock_Unidades"].sum()),
        "proveedores": int(len(data.proveedores)),
    }


if __name__ == "__main__":
    import json

    data = connect()
    print("=== dashboard_lanas_excel — resumen ===")
    print(json.dumps(summary(data), indent=2, ensure_ascii=False))
    print(f"\nVentas ({len(data.ventas)} filas):")
    print(data.ventas.to_string(index=False))
    print(f"\nInventario ({len(data.inventario)} filas):")
    print(data.inventario.to_string(index=False))
    print(f"\nProveedores ({len(data.proveedores)} filas):")
    print(data.proveedores.to_string(index=False))
