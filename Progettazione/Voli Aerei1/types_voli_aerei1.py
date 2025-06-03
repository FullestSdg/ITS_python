from typing import Type, Self

class RealGTZ(float):

    def new(cls, v: int | float | str | bool | Self) -> Self:
        
        n: float = super().new(cls, v)

        if n > 0:
            return n

        raise ValueError(f"Il numero inserito {v}è negativo o zero!")
    
class RealGEZ(float):
    # Tipo di dato Reale >= 0

    def new(cls, v: int | float | str | bool | Self) -> Self:
        # Invoco il metodo new della superclasse, che è 'float'
        n: float = super().new(cls, v)

        if n >= 0:
            return n

        raise ValueError(f"Il numero inserito {v} è negativo!")
