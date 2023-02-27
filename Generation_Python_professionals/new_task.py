def from_hex_to_rgb(color: str) -> tuple:
    return tuple(map(lambda x: int(x, 16), [color[1:3], color[3:5], color[5:]]))


if __name__ == '__main__':

    colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50', '#CD5C5C', '#F08080', '#E9967A',
              '#FA8072', '#FFA07A', '#FF4500', '#FF8C00', '#FFA500', '#FFD700', '#B8860B', '#DAA520',
              '#EEE8AA', '#BDB76B', '#F0E68C', '#808000', '#FFFF00', '#9ACD32', '#556B2F', '#6B8E23',
              '#7CFC00', '#7FFF00', '#ADFF2F']

    for red, green, blue in map(from_hex_to_rgb, colors):
        print(f"Red={red}, Green={green}, Blue={blue}")
