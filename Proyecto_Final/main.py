import tkinter as tk
from tkinter import messagebox, simpledialog
from empleados.empleado import Empleado
from producto.producto import Producto
from pedido.pedido import Pedido
from factura.factura import Factura

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión")
        self.geometry("300x200")
        self.current_frame = None
        self.show_login()

    def show_frame(self, frame_class):
        """Muestra un nuevo frame y oculta el actual"""
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        self.current_frame = frame_class(self)
        self.current_frame.pack()

    def show_login(self):
        self.show_frame(LoginFrame)

    def show_menu(self):
        self.show_frame(MenuFrame)

class LoginFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_login_widgets()

    def create_login_widgets(self):
        tk.Label(self, text="Correo Electrónico:").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        tk.Label(self, text="Contraseña:").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)
        tk.Button(self, text="Iniciar Sesión", command=self.login).pack(pady=10)
        tk.Button(self, text="Registrar Nuevo Empleado", command=self.register_employee).pack(pady=10)

    def login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        if Empleado.login(email, password):
            self.parent.show_menu()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def register_employee(self):
        self.parent.show_frame(RegisterEmployeeFrame)

class MenuFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_menu_widgets()

    def create_menu_widgets(self):
        tk.Button(self, text="Gestionar Productos", command=lambda: self.parent.show_frame(ProductManagementFrame)).pack(pady=10)
        tk.Button(self, text="Gestionar Empleados", command=lambda: self.parent.show_frame(RegisterEmployeeFrame)).pack(pady=10)
        tk.Button(self, text="Gestionar Pedidos", command=lambda: self.parent.show_frame(OrderManagementFrame)).pack(pady=10)
        tk.Button(self, text="Generar Factura", command=lambda: self.parent.show_frame(InvoiceGenerationFrame)).pack(pady=10)
        tk.Button(self, text="Cerrar Sesión", command=self.logout).pack(pady=10)

    def logout(self):
        self.parent.show_login()

class RegisterEmployeeFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_employee_form()

    def create_employee_form(self):
        tk.Label(self, text="Nombre:").pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)
        tk.Label(self, text="Correo Electrónico:").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        tk.Label(self, text="Puesto:").pack(pady=5)
        self.position_entry = tk.Entry(self)
        self.position_entry.pack(pady=5)
        tk.Label(self, text="Contraseña:").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)
        tk.Button(self, text="Registrar", command=self.register).pack(pady=10)
        tk.Button(self, text="Regresar", command=lambda: self.parent.show_menu()).pack(pady=10)

    def register(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        position = self.position_entry.get().strip()
        password = self.password_entry.get().strip()
        if all([name, email, position, password]):
            employee = Empleado(nombre=name, email=email, puesto=position, contrasena=password)
            try:
                employee.create()
                messagebox.showinfo("Éxito", "Empleado registrado con éxito")
                self.parent.show_menu()
            except Exception as e:
                messagebox.showerror("Error", f"Error al registrar el empleado: {str(e)}")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

class ProductManagementFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_product_management_widgets()

    def create_product_management_widgets(self):
        tk.Label(self, text="Aquí puedes gestionar los productos").pack(pady=20)
        tk.Button(self, text="Agregar Producto", command=self.add_product).pack(pady=10)
        tk.Button(self, text="Ver Productos", command=self.view_products).pack(pady=10)
        tk.Button(self, text="Eliminar Producto", command=self.delete_product).pack(pady=10)
        tk.Button(self, text="Actualizar Producto", command=self.update_product).pack(pady=10)
        tk.Button(self, text="Regresar", command=lambda: self.parent.show_menu()).pack(pady=10)

    def add_product(self):
        new_window = tk.Toplevel(self)
        new_window.title("Agregar Producto")

        tk.Label(new_window, text="Nombre:").pack(pady=5)
        name_entry = tk.Entry(new_window)
        name_entry.pack(pady=5)

        tk.Label(new_window, text="Precio:").pack(pady=5)
        price_entry = tk.Entry(new_window)
        price_entry.pack(pady=5)

        tk.Label(new_window, text="Inventario:").pack(pady=5)
        inventory_entry = tk.Entry(new_window)
        inventory_entry.pack(pady=5)

        def save_product():
            name = name_entry.get().strip()
            price = float(price_entry.get().strip())
            inventory = int(inventory_entry.get().strip())
            if name and price >= 0 and inventory >= 0:
                product = Producto(nombre=name, precio=price, inventario=inventory)
                try:
                    product.create()
                    messagebox.showinfo("Éxito", "Producto agregado con éxito")
                    new_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Error al agregar el producto: {str(e)}")
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos correctamente.")

        tk.Button(new_window, text="Guardar", command=save_product).pack(pady=10)

    def view_products(self):
        products = Producto.get_all()
        product_info = "\n".join([f"ID: {p.id}, Nombre: {p.nombre}, Precio: {p.precio}, Inventario: {p.inventario}" for p in products])
        messagebox.showinfo("Productos", product_info or "No hay productos disponibles.")

    def delete_product(self):
        product_id = simpledialog.askinteger("Eliminar Producto", "Ingrese el ID del producto a eliminar:")
        if product_id:
            try:
                Producto.delete(product_id)
                messagebox.showinfo("Éxito", "Producto eliminado con éxito")
            except Exception as e:
                messagebox.showerror("Error", f"Error al eliminar el producto: {str(e)}")

    def update_product(self):
        product_id = simpledialog.askinteger("Actualizar Producto", "Ingrese el ID del producto a actualizar:")
        if product_id:
            new_window = tk.Toplevel(self)
            new_window.title("Actualizar Producto")

            tk.Label(new_window, text="Nuevo Nombre:").pack(pady=5)
            new_name_entry = tk.Entry(new_window)
            new_name_entry.pack(pady=5)

            tk.Label(new_window, text="Nuevo Precio:").pack(pady=5)
            new_price_entry = tk.Entry(new_window)
            new_price_entry.pack(pady=5)

            tk.Label(new_window, text="Nuevo Inventario:").pack(pady=5)
            new_inventory_entry = tk.Entry(new_window)
            new_inventory_entry.pack(pady=5)

            def save_updated_product():
                new_name = new_name_entry.get().strip()
                new_price = float(new_price_entry.get().strip())
                new_inventory = int(new_inventory_entry.get().strip())
                if new_name and new_price >= 0 and new_inventory >= 0:
                    try:
                        Producto.update(product_id, new_name, new_price, new_inventory)
                        messagebox.showinfo("Éxito", "Producto actualizado con éxito")
                        new_window.destroy()
                    except Exception as e:
                        messagebox.showerror("Error", f"Error al actualizar el producto: {str(e)}")
                else:
                    messagebox.showerror("Error", "Por favor, complete todos los campos correctamente.")

            tk.Button(new_window, text="Guardar", command=save_updated_product).pack(pady=10)

class OrderManagementFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_order_management_widgets()

    def create_order_management_widgets(self):
        tk.Label(self, text="Aquí puedes gestionar los pedidos").pack(pady=20)
        tk.Button(self, text="Agregar Pedido", command=self.add_order).pack(pady=10)
        tk.Button(self, text="Ver Pedidos", command=self.view_orders).pack(pady=10)
        tk.Button(self, text="Eliminar Pedido", command=self.delete_order).pack(pady=10)
        tk.Button(self, text="Actualizar Pedido", command=self.update_order).pack(pady=10)
        tk.Button(self, text="Regresar", command=lambda: self.parent.show_menu()).pack(pady=10)

    def add_order(self):
        new_window = tk.Toplevel(self)
        new_window.title("Agregar Pedido")

        tk.Label(new_window, text="ID del Producto:").pack(pady=5)
        product_id_entry = tk.Entry(new_window)
        product_id_entry.pack(pady=5)

        tk.Label(new_window, text="Cantidad:").pack(pady=5)
        quantity_entry = tk.Entry(new_window)
        quantity_entry.pack(pady=5)

        def save_order():
            product_id = int(product_id_entry.get().strip())
            quantity = int(quantity_entry.get().strip())
            if product_id >= 0 and quantity > 0:
                order = Pedido(producto_id=product_id, cantidad=quantity)
                try:
                    order.create()
                    messagebox.showinfo("Éxito", "Pedido agregado con éxito")
                    new_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Error al agregar el pedido: {str(e)}")
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos correctamente.")

        tk.Button(new_window, text="Guardar", command=save_order).pack(pady=10)

    def view_orders(self):
        orders = Pedido.get_all()
        order_info = "\n".join([f"ID: {o.id}, Producto ID: {o.producto_id}, Cantidad: {o.cantidad}" for o in orders])
        messagebox.showinfo("Pedidos", order_info or "No hay pedidos disponibles.")

    def delete_order(self):
        order_id = simpledialog.askinteger("Eliminar Pedido", "Ingrese el ID del pedido a eliminar:")
        if order_id:
            try:
                Pedido.delete(order_id)
                messagebox.showinfo("Éxito", "Pedido eliminado con éxito")
            except Exception as e:
                messagebox.showerror("Error", f"Error al eliminar el pedido: {str(e)}")

    def update_order(self):
        order_id = simpledialog.askinteger("Actualizar Pedido", "Ingrese el ID del pedido a actualizar:")
        if order_id:
            new_window = tk.Toplevel(self)
            new_window.title("Actualizar Pedido")

            tk.Label(new_window, text="Nueva Cantidad:").pack(pady=5)
            new_quantity_entry = tk.Entry(new_window)
            new_quantity_entry.pack(pady=5)

            def save_updated_order():
                new_quantity = int(new_quantity_entry.get().strip())
                if new_quantity > 0:
                    try:
                        Pedido.update(order_id, new_quantity)
                        messagebox.showinfo("Éxito", "Pedido actualizado con éxito")
                        new_window.destroy()
                    except Exception as e:
                        messagebox.showerror("Error", f"Error al actualizar el pedido: {str(e)}")
                else:
                    messagebox.showerror("Error", "Por favor, complete todos los campos correctamente.")

            tk.Button(new_window, text="Guardar", command=save_updated_order).pack(pady=10)

class InvoiceGenerationFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_invoice_generation_widgets()

    def create_invoice_generation_widgets(self):
        tk.Label(self, text="Generar Factura").pack(pady=20)
        tk.Button(self, text="Generar Nueva Factura", command=self.generate_invoice).pack(pady=10)
        tk.Button(self, text="Ver Facturas", command=self.view_invoices).pack(pady=10)
        tk.Button(self, text="Regresar", command=lambda: self.parent.show_menu()).pack(pady=10)

    def generate_invoice(self):
        order_id = simpledialog.askinteger("Generar Factura", "Ingrese el ID del pedido:")
        if order_id:
            try:
                factura = Factura(pedido_id=order_id)
                factura.create()
                messagebox.showinfo("Éxito", "Factura generada con éxito")
            except Exception as e:
                messagebox.showerror("Error", f"Error al generar la factura: {str(e)}")

    def view_invoices(self):
        invoices = Factura.get_all()
        invoice_info = "\n".join([f"ID: {i.id}, Pedido ID: {i.pedido_id}, Fecha: {i.fecha}" for i in invoices])
        messagebox.showinfo("Facturas", invoice_info or "No hay facturas disponibles.")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
