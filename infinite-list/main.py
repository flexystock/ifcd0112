class InfiniteList:
    def __init__(self, *args, fill_value=None):
        self.fill_value = fill_value
        if len(args) == 1 and isinstance(args[0], (list, tuple, set)):
            self.items = list(args[0])
        else:
            self.items = list(args)

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self.items))
            # Delegar al slicing de la lista interna o manejar extensión si fuera necesario
            sliced_items = self.items[index]
            # Si el slice abarca más allá del tamaño, rellenar con fill_value
            if index.stop is not None and index.stop > len(self.items):
                extra_count = index.stop - max(len(self.items), start)
                sliced_items.extend([self.fill_value] * extra_count)
            return sliced_items

        if index >= len(self.items):
            return self.fill_value
        return self.items[index]

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            # Manejar asignación con slices si es requerido
            self.items[index] = value
            return

        if index >= len(self.items):
            extension_size = index - len(self.items) + 1
            self.items.extend([self.fill_value] * extension_size)
        self.items[index] = value

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return ",".join(str(x) for x in self.items)
