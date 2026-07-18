from app.database import SessionLocal
from app.models.marca import Marca
from app.models.modelo import Modelo


def seed_data():
    db = SessionLocal()

    try:
        # Evitar duplicar si ya se corrió antes
        if db.query(Marca).first():
            print("Ya hay datos cargados, no se vuelve a sembrar.")
            return

        marcas_y_modelos = {
            "Toyota": ["Corolla", "Hilux", "Etios", "Yaris"],
            "Ford": ["Fiesta", "Focus", "Ranger", "EcoSport"],
            "Volkswagen": ["Gol", "Polo", "Amarok", "Vento"],
            "Chevrolet": ["Onix", "Cruze", "S10", "Tracker"],
            "Fiat": ["Cronos", "Argo", "Toro", "Palio"],
            "Renault": ["Sandero", "Duster", "Kangoo", "Logan"],
        }

        for nombre_marca, modelos in marcas_y_modelos.items():
            marca = Marca(nombre=nombre_marca)
            db.add(marca)
            db.flush()  # asigna el id a `marca` sin hacer commit todavía

            for nombre_modelo in modelos:
                modelo = Modelo(nombre=nombre_modelo, marca_id=marca.id)
                db.add(modelo)

        db.commit()
        print("Datos de prueba cargados correctamente ✅")

    except Exception as e:
        db.rollback()
        print(f"Error al cargar datos: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_data()