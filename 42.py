# calcular quanta agua da chuva pode ser armazenada depois que chove
# no espaço que sera dado

class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Calcula a quantidade de água da chuva que pode ser retida entre as barras 
        usando o método otimizado de Two Pointers.
        """
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        trapped_water = 0

        while left < right:
            if height[left] < height[right]:
                # O limite é o lado esquerdo
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    trapped_water += max_left - height[left]
                
                left += 1
            else:
                # O limite é o lado direito
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    trapped_water += max_right - height[right]
                
                right -= 1

        return trapped_water