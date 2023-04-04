from field import Field
import field_debug

grid_8 = Field(8)

grid_8.print_grid()

print(len(grid_8.grid))

for i in range(len(grid_8.grid)):
    print(len(grid_8.grid[i]))