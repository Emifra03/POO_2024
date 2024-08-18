import tkinter as tk
from tkinter import messagebox, simpledialog
from empleado import Empleado
from producto import Producto
from pedido import Pedido

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión")
        self.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="Gestión de Productos", command=self.open_product_management).pack(pady=10)
        tk.Button(self, text="Gestión de Pedidos", command=self.open_order_management).pack(pady=10)
        tk.Button(self, text="Gestión de Empleados", command=self.open_employee_management).pack(pady=10)

    def open_product_management(self):
        ProductManagementWindow(self)

    def open_order_management(self):
        OrderManagementWindow(self)

    def open_employee_management(self):
        EmployeeManagementWindow(self)

class OrderManagementWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestión de Pedidos")
        self.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="Agregar Pedido", command=lambda: OrderForm(self, action='create')).pack(pady=5)
        tk.Button(self, text="Ver Pedido", command=self.view_order).pack(pady=5)
        tk.Button(self, text="Actualizar Pedido", command=lambda: OrderForm(self, action='update')).pack(pady=5)
        tk.Button(self, text="Eliminar Pedido", command=self.delete_order).pack(pady=5)
        tk.Button(self, text="Regresar", command=self.destroy).pack(pady=10)

    def view_order(self):
        order_id = simpledialog.askinteger("Ver Pedido", "Ingrese el ID del pedido:")
        if order_id:
            try:
                order = Pedido().read(order_id)
                if order:
                    messagebox.showinfo("Pedido", f"ID: {order[0]}\nFecha: {order[1]}\nDetalle: {order[2]}\nCantidad: {order[3]}\nID Empleado: {order[4]}")
                else:
                    messagebox.showerror("Error", "Pedido no encontrado")
            except Exception as e:
                messagebox.showerror("Error", f"Error al leer el pedido: {str(e)}")

    def delete_order(self):
        order_id = simpledialog.askinteger("Eliminar Pedido", "Ingrese el ID del pedido:")
        if order_id:
            try:
                Pedido().delete(order_id)
                messagebox.showinfo("Éxito", "Pedido eliminado con éxito")
            except Exception as e:
                messagebox.showerror("Error", f"Error al eliminar el pedido: {str(e)}")

class OrderForm(tk.Toplevel):
    def __init__(self, parent, action, order_id=None):
        super().__init__(parent)
        self.title(f"{action.capitalize()} Pedido")
        self.geometry("300x300")
        self.action = action
        self.order_id = order_id
        self.create_form()

    def create_form(self):
        tk.Label(self, text="Fecha:").pack(pady=5)
        self.date_entry = tk.Entry(self)
        self.date_entry.pack(pady=5)
        
        tk.Label(self, text="Detalle:").pack(pady=5)
        self.detail_entry = tk.Entry(self)
        self.detail_entry.pack(pady=5)
        
        tk.Label(self, text="Cantidad:").pack(pady=5)
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.pack(pady=5)
        
        tk.Label(self, text="ID Empleado:").pack(pady=5)
        self.employee_id_entry = tk.Entry(self)
        self.employee_id_entry.pack(pady=5)

        if self.action == 'update' and self.order_id:
            try:
                order = Pedido().read(self.order_id)
                if order:
                    self.date_entry.insert(0, order[1])
                    self.detail_entry.insert(0, order[2])
                    self.quantity_entry.insert(0, order[3])
                    self.employee_id_entry.insert(0, order[4])
                else:
                    messagebox.showerror("Error", "Pedido no encontrado")
                    self.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error al leer el pedido: {str(e)}")
                self.destroy()

        tk.Button(self, text=f"{self.action.capitalize()} Pedido", command=self.submit).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.destroy).pack(pady=10)

    def submit(self):
        date = self.date_entry.get().strip()
        detail = self.detail_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        employee_id = self.employee_id_entry.get().strip()

        if all([date, detail, quantity, employee_id]):
            try:
                if self.action == 'create':
                    order = Pedido(fecha=date, detalle=detail, cantidad=quantity, id_empleado=employee_id)
                    order.create()
                    messagebox.showinfo("Éxito", "Pedido creado con éxito")
                elif self.action == 'update' and self.order_id:
                    Pedido().update(self.order_id, date, detail, quantity, employee_id)
                    messagebox.showinfo("Éxito", "Pedido actualizado con éxito")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error al {self.action} el pedido: {str(e)}")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

class ProductManagementWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestión de Productos")
        self.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="Agregar Producto", command=lambda: ProductForm(self, action='create')).pack(pady=5)
        tk.Button(self, text="Ver Producto", command=self.view_product).pack(pady=5)
        tk.Button(self, text="Actualizar Producto", command=lambda: ProductForm(self, action='update')).pack(pady=5)
        tk.Button(self, text="Eliminar Producto", command=self.delete_product).pack(pady=5)
        tk.Button(self, text="Regresar", command=self.destroy).pack(pady=10)

    def view_product(self):
        product_id = simpledialog.askinteger("Ver Producto", "Ingrese el ID del producto:")
        if product_id:
            try:
                product = Producto().read(product_id)
                if product:
                    messagebox.showinfo("Producto", f"ID: {product[0]}\nNombre: {product[1]}\nDescripción: {product[2]}\nPrecio: {product[3]}\nStock: {product[4]}")
                else:
                    messagebox.showerror("Error", "Producto no encontrado")
            except Exception as e:
                messagebox.showerror("Error", f"Error al leer el producto: {str(e)}")

    def delete_product(self):
        product_id = simpledialog.askinteger("Eliminar Producto", "Ingrese el ID del producto:")
        if product_id:
            try:
                Producto().delete(product_id)
                messagebox.showinfo("Éxito", "Producto eliminado con éxito")
            except Exception as e:
                messagebox.showerror("Error", f"Error al eliminar el producto: {str(e)}")

class ProductForm(tk.Toplevel):
    def __init__(self, parent, action, product_id=None):
        super().__init__(parent)
        self.title(f"{action.capitalize()} Producto")
        self.geometry("300x300")
        self.action = action
        self.product_id = product_id
        self.create_form()

    def create_form(self):
        tk.Label(self, text="Nombre:").pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)
        
        tk.Label(self, text="Descripción:").pack(pady=5)
        self.description_entry = tk.Entry(self)
        self.description_entry.pack(pady=5)
        
        tk.Label(self, text="Precio:").pack(pady=5)
        self.price_entry = tk.Entry(self)
        self.price_entry.pack(pady=5)
        
        tk.Label(self, text="Stock:").pack(pady=5)
        self.stock_entry = tk.Entry(self)
        self.stock_entry.pack(pady=5)

        if self.action == 'update' and self.product_id:
            try:
                product = Producto().read(self.product_id)
                if product:
                    self.name_entry.insert(0, product[1])
                    self.description_entry.insert(0, product[2])
                    self.price_entry.insert(0, product[3])
                    self.stock_entry.insert(0, product[4])
                else:
                    messagebox.showerror("Error", "Producto no encontrado")
                    self.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error al leer el producto: {str(e)}")
                self.destroy()

        tk.Button(self, text=f"{self.action.capitalize()} Producto", command=self.submit).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.destroy).pack(pady=10)

    def submit(self):
        name = self.name_entry.get().strip()
        description = self.description_entry.get().strip()
        price = self.price_entry.get().strip()
        stock = self.stock_entry.get().strip()

        if all([name, description, price, stock]):
            try:
                if self.action == 'create':
                    product = Producto(nombre=name, descripcion=description, precio=price, stock=stock)
                    product.create()
                    messagebox.showinfo("Éxito", "Producto creado con éxito")
                elif self.action == 'update' and self.product_id:
                    Producto().update(self.product_id, name, description, price, stock)
                    messagebox.showinfo("Éxito", "Producto actualizado con éxito")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error al {self.action} el producto: {str(e)}")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

class EmployeeManagementWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestión de Empleados")
        self.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="Agregar Empleado", command=lambda: EmployeeForm(self, action='create')).pack(pady=5)
        tk.Button(self, text="Ver Empleado", command=self.view_employee).pack(pady=5)
        tk.Button(self, text="Actualizar Empleado", command=lambda: EmployeeForm(self, action='update')).pack(pady=5)
        tk.Button(self, text="Eliminar Empleado", command=self.delete_employee).pack(pady=5)
        tk.Button(self, text="Regresar", command=self.destroy).pack(pady=10)

    def view_employee(self):
        employee_id = simpledialog.askinteger("Ver Empleado", "Ingrese el ID del empleado:")
        if employee_id:
            try:
                employee = Empleado().read(employee_id)
                if employee:
                    messagebox.showinfo("Empleado", f"ID: {employee[0]}\nNombre: {employee[1]}\nRol: {employee[2]}")
                else:
                    messagebox.showerror("Error", "Empleado no encontrado")
            except Exception as e:
                messagebox.showerror("Error", f"Error al leer el empleado: {str(e)}")

    def delete_employee(self):
        employee_id = simpledialog.askinteger("Eliminar Empleado", "Ingrese el ID del empleado:")
        if employee_id:
            try:
                Empleado().delete(employee_id)
                messagebox.showinfo("Éxito", "Empleado eliminado con éxito")
            except Exception as e:
                messagebox.showerror("Error", f"Error al eliminar el empleado: {str(e)}")

class EmployeeForm(tk.Toplevel):
    def __init__(self, parent, action, employee_id=None):
        super().__init__(parent)
        self.title(f"{action.capitalize()} Empleado")
        self.geometry("300x300")
        self.action = action
        self.employee_id = employee_id
        self.create_form()

    def create_form(self):
        tk.Label(self, text="Nombre:").pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)
        
        tk.Label(self, text="Rol:").pack(pady=5)
        self.role_entry = tk.Entry(self)
        self.role_entry.pack(pady=5)
        
        tk.Label(self, text="Contraseña:").pack(pady=5)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(pady=5)

        if self.action == 'update' and self.employee_id:
            try:
                employee = Empleado().read(self.employee_id)
                if employee:
                    self.name_entry.insert(0, employee[1])
                    self.role_entry.insert(0, employee[2])
                else:
                    messagebox.showerror("Error", "Empleado no encontrado")
                    self.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error al leer el empleado: {str(e)}")
                self.destroy()

        tk.Button(self, text=f"{self.action.capitalize()} Empleado", command=self.submit).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.destroy).pack(pady=10)

    def submit(self):
        name = self.name_entry.get().strip()
        role = self.role_entry.get().strip()
        password = self.password_entry.get().strip()

        if all([name, role, password]):
            try:
                if self.action == 'create':
                    employee = Empleado(nombre=name, rol=role, contrasena=password)
                    employee.create()
                    messagebox.showinfo("Éxito", "Empleado creado con éxito")
                elif self.action == 'update' and self.employee_id:
                    Empleado().update(self.employee_id, name, role, password)
                    messagebox.showinfo("Éxito", "Empleado actualizado con éxito")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error al {self.action} el empleado: {str(e)}")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
