from PyQt6.QtWidgets import *
from gui import *
import math


class Logic(QMainWindow, Ui_MainWindow):
    """Class to display a GUI calculator containing basic calculation functions
    in addition to volumetric and area calculations for specified shapes."""
    def __init__(self):
        """enables all calculator buttons and hides advanced functions"""
        super().__init__()
        self.setupUi(self)
        self.label.clear()
        self.label_result.clear()

        self.button_clear.clicked.connect(lambda: self.clear_button())
        self.button_area.clicked.connect(lambda: self.area_button())
        self.button_volume.clicked.connect(lambda: self.volume_button())
        self.button_memory.clicked.connect(lambda: self.memory_button())

        self.button_num0.clicked.connect(lambda: self.button_0())
        self.button_num1.clicked.connect(lambda: self.button_1())
        self.button_num2.clicked.connect(lambda: self.button_2())
        self.button_num3.clicked.connect(lambda: self.button_3())
        self.button_num4.clicked.connect(lambda: self.button_4())
        self.button_num5.clicked.connect(lambda: self.button_5())
        self.button_num6.clicked.connect(lambda: self.button_6())
        self.button_num7.clicked.connect(lambda: self.button_7())
        self.button_num8.clicked.connect(lambda: self.button_8())
        self.button_num9.clicked.connect(lambda: self.button_9())

        self.button_add.clicked.connect(lambda: self.add_button())
        self.button_minus.clicked.connect(lambda: self.subtract_button())
        self.button_multiply.clicked.connect(lambda: self.multiply_button())
        self.button_divide.clicked.connect(lambda: self.divide_button())
        self.button_equal.clicked.connect(lambda: self.equal_button())
        self.button_plusMinus.clicked.connect(lambda: self.plus_minus_button())
        self.button_delete.clicked.connect(lambda: self.delete_button())
        self.button_decimal.clicked.connect(lambda: self.decimal_button())

        self.radio_circle.clicked.connect(lambda: self.circ_click())
        self.radio_rectangle.clicked.connect(lambda: self.rectangle_click())
        self.radio_triangle.clicked.connect(lambda: self.triangle_click())
        self.radio_sphere.clicked.connect(lambda: self.sphere_click())
        self.radio_cube.clicked.connect(lambda: self.cube_click())
        self.radio_cone.clicked.connect(lambda: self.cone_click())

        self.buttonSubmit1.clicked.connect(lambda: self.submit1())
        self.buttonSubmit2.clicked.connect(lambda: self.submit2())
        self.buttonSubmit3.clicked.connect(lambda: self.submit3())

        self.radio_circle.hide()
        self.radio_rectangle.hide()
        self.radio_triangle.hide()
        self.radio_sphere.hide()
        self.radio_cube.hide()
        self.radio_cone.hide()

        self.label_input1.hide()
        self.label_input2.hide()
        self.label_input3.hide()

        self.buttonSubmit1.hide()
        self.buttonSubmit2.hide()
        self.buttonSubmit3.hide()

        self.inputText1.hide()
        self.inputText2.hide()
        self.inputText3.hide()

    def clear_button(self) -> None:
        """clears all input and sets calculator back to default settings"""
        self.label.clear()
        self.label_result.clear()
        self.radio_circle.hide()
        self.radio_rectangle.hide()
        self.radio_triangle.hide()
        self.radio_sphere.hide()
        self.radio_cube.hide()
        self.radio_cone.hide()
        self.label_input1.hide()
        self.label_input2.hide()
        self.label_input3.hide()
        self.inputText1.hide()
        self.inputText2.hide()
        self.inputText3.hide()
        self.buttonSubmit1.hide()
        self.buttonSubmit2.hide()
        self.buttonSubmit3.hide()
        self.enable_num_pad()
        self.enable_operations()

    def area_button(self) -> None:
        """Disables basic calculator functions and enables
        area calculation buttons and text input boxes based on
        selected shape"""
        self.label.clear()
        self.label_result.clear()
        self.radio_sphere.hide()
        self.radio_cube.hide()
        self.radio_cone.hide()
        self.reset()
        self.radio_circle.show()
        self.radio_rectangle.show()
        self.radio_triangle.show()
        self.disable_num_pad()
        self.disable_operations()

    def volume_button(self) -> None:
        """Disables basic calculator functions and enables
        volumetric calculation buttons and text input boxes based on
        selected shape"""
        self.label.clear()
        self.label_result.clear()
        self.radio_sphere.show()
        self.radio_cube.show()
        self.radio_cone.show()
        self.reset()
        self.radio_circle.hide()
        self.radio_rectangle.hide()
        self.radio_triangle.hide()
        self.disable_num_pad()
        self.disable_operations()

    def memory_button(self) -> None:
        """updates the display to the previously calculated value
        to continue operations. some functions are disabled to ensure proper
        operations can be performed"""
        memory = self.label_result.text()
        if memory == 'Invalid Input':
            pass
        else:
            self.label.setText(memory)
            self.label_result.clear()
            self.disable_num_pad()

    def disable_num_pad(self) -> None:
        """disables the number pad"""
        self.button_num0.setEnabled(False)
        self.button_num1.setEnabled(False)
        self.button_num2.setEnabled(False)
        self.button_num3.setEnabled(False)
        self.button_num4.setEnabled(False)
        self.button_num5.setEnabled(False)
        self.button_num6.setEnabled(False)
        self.button_num7.setEnabled(False)
        self.button_num8.setEnabled(False)
        self.button_num9.setEnabled(False)
        self.button_plusMinus.setEnabled(False)
        self.button_decimal.setEnabled(False)

    def enable_num_pad(self) -> None:
        """enables the number pad"""
        self.button_num0.setEnabled(True)
        self.button_num1.setEnabled(True)
        self.button_num2.setEnabled(True)
        self.button_num3.setEnabled(True)
        self.button_num4.setEnabled(True)
        self.button_num5.setEnabled(True)
        self.button_num6.setEnabled(True)
        self.button_num7.setEnabled(True)
        self.button_num8.setEnabled(True)
        self.button_num9.setEnabled(True)
        self.button_plusMinus.setEnabled(True)
        self.button_decimal.setEnabled(True)

    def disable_operations(self) -> None:
        """disables the operations buttons"""
        self.button_add.setEnabled(False)
        self.button_minus.setEnabled(False)
        self.button_divide.setEnabled(False)
        self.button_multiply.setEnabled(False)
        self.button_plusMinus.setEnabled(False)
        self.button_decimal.setEnabled(False)
        self.button_equal.setEnabled(False)
        self.button_delete.setEnabled(False)
        self.button_memory.setEnabled(False)

    def enable_operations(self) -> None:
        """enables operation buttons"""
        self.button_add.setEnabled(True)
        self.button_minus.setEnabled(True)
        self.button_divide.setEnabled(True)
        self.button_multiply.setEnabled(True)
        self.button_plusMinus.setEnabled(True)
        self.button_decimal.setEnabled(True)
        self.button_equal.setEnabled(True)
        self.button_delete.setEnabled(True)
        self.button_memory.setEnabled(True)

    def button_0(self) -> None:
        """adds a 0 to the display"""
        display = str(self.label.text())
        self.label.setText(f'{display}' + '0')

    def button_1(self) -> None:
        """adds a 1 to the display"""
        display = self.label.text()
        self.label.setText(f'{display}' + '1')

    def button_2(self) -> None:
        """adds a 2 to the display"""
        display = str(self.label.text())
        self.label.setText(f'{display}' + '2')

    def button_3(self) -> None:
        """adds a 3 to the display"""
        display = str(self.label.text())
        self.label.setText(f'{display}' + '3')

    def button_4(self) -> None:
        """adds a 4 to the display"""
        display = str(self.label.text())
        self.label.setText(f'{display}' + '4')

    def button_5(self) -> None:
        """adds a 5 to the display"""
        display = str(self.label.text())
        self.label.setText(f'{display}' + '5')

    def button_6(self) -> None:
        """adds a 6 to the display"""
        display = str(self.label.text())
        self.label.setText(f'{display}' + '6')

    def button_7(self) -> None:
        """adds a 7 to the display"""
        display = str(self.label.text())
        self.label.setText(f'{display}' + '7')

    def button_8(self) -> None:
        """adds an 8 to the display"""
        display = str(self.label.text())
        self.label.setText(f'{display}' + '8')

    def button_9(self) -> None:
        """adds a 9 to the display"""
        display = str(self.label.text())
        self.label.setText(f'{display}' + '9')

    def add_button(self) -> None:
        """adds a plus to the display"""
        display = self.label.text()
        alt_display = display.split(' ')
        if display == '':
            pass
        elif float(alt_display[0]) < 0:
            self.label.setText(f'{display}' + ' + ')
        elif '+' in display or '-' in display or '*' in display or '/' in display:
            pass
        else:
            self.label.setText(f'{display}' + ' + ')
        self.enable_num_pad()

    def subtract_button(self) -> None:
        """adds a minus to the display"""
        display = str(self.label.text())
        alt_display = display.split(' ')
        if display == '':
            pass
        elif float(alt_display[0]) < 0:
            self.label.setText(f'{display}' + ' + ')
        elif '+' in display or '-' in display or '*' in display or '/' in display:
            pass
        else:
            self.label.setText(f'{display}' + ' - ')
        self.enable_num_pad()

    def multiply_button(self) -> None:
        """adds a multiplication to the display"""
        display = self.label.text()
        alt_display = display.split(' ')
        if display == '':
            pass
        elif float(alt_display[0]) < 0:
            self.label.setText(f'{display}' + ' + ')
        elif '+' in display or '-' in display or '*' in display or '/' in display:
            pass
        else:
            self.label.setText(f'{display}' + ' * ')
        self.enable_num_pad()

    def divide_button(self) -> None:
        """adds a division to the display"""
        display = self.label.text()
        alt_display = display.split(' ')
        if display == '':
            pass
        elif float(alt_display[0]) < 0:
            self.label.setText(f'{display}' + ' + ')
        elif '+' in display or '-' in display or '*' in display or '/' in display:
            pass
        else:
            self.label.setText(f'{display}' + ' / ')
        self.enable_num_pad()

    def equal_button(self) -> None:
        """ splits the display into three strings and uses the middle string
        to determine which basic operation to perform then push the result
        to the memory display"""
        display = (self.label.text()).split(' ')
        try:
            num1 = float(display[0])
            num2 = float(display[2])
            action = display[1]
        except IndexError:
            self.label_result.setText(display[0])
            self.label.clear()
        except ValueError:
            self.label_result.setText('Invalid Input')
            self.label.clear()
        else:
            if len(display) == 1:
                self.label.setText(num1)
            elif action == '+':
                total = num1 + num2
                self.label_result.setText(str(total))
                self.label.clear()
            elif action == '-':
                total = num1 - num2
                self.label_result.setText(str(total))
                self.label.clear()
            elif action == '*':
                total = num1 * num2
                self.label_result.setText(str(total))
                self.label.clear()
            elif action == '/':
                total = num1 / num2
                self.label_result.setText(str(total))
                self.label.clear()
        finally:
            self.enable_num_pad()

    def plus_minus_button(self) -> None:
        """adds a negative sign in front of the last
        digit in the display"""
        display = self.label.text()
        if display == '':
            self.label.setText('-')

        elif len(display.split()) == 1 and display != '':
            self.label.setText('-' + display)

        elif len(display.split()) < 3:
            self.label.setText(display + '-')

    def decimal_button(self) -> None:
        """adds a decimal to the display after the last input digit"""
        display = str(self.label.text())
        alt_display = display.split(' ')
        if display == '':
            self.label.setText('0.')
        elif alt_display[-1] == '':
            self.label.setText(f'{display}' + '0.')
        else:
            self.label.setText(f'{display}' + '.')

    def delete_button(self) -> None:
        """deletes the last input into the display"""
        display = self.label.text()
        if display == '':
            pass
        elif len(display.split()) == 1 and display != '':
            self.label.setText('')
        elif len(display.split()) == 2 and display != '':
            display = display.split()
            self.label.setText(display[0] + ' ')
        else:
            display = display.split()
            self.label.setText(display[0] + ' ' + display[1] + ' ')
        self.enable_num_pad()
        self.enable_operations()

    def reset(self) -> None:
        """clears text input, display and submit buttons for
        advanced calculation features
        """
        self.inputText1.setText('')
        self.inputText1.hide()
        self.inputText2.setText('')
        self.inputText2.hide()
        self.inputText3.setText('')
        self.inputText3.hide()
        self.label_input1.setText('')
        self.label_input1.hide()
        self.label_input2.setText('')
        self.label_input2.hide()
        self.label_input3.setText('')
        self.label_input3.hide()
        self.buttonSubmit1.hide()
        self.buttonSubmit2.hide()
        self.buttonSubmit3.hide()

    def circ_click(self) -> None:
        """enables calculation criteria input boxes
        for a circle"""
        self.reset()
        self.label_input1.show()
        self.label_input1.setText('Radius')
        self.inputText1.show()
        self.inputText1.setText('')
        self.buttonSubmit1.show()

    def circle_area(self) -> None:
        """calculates the area of circle"""
        self.label.clear()
        radius = float(self.inputText1.text())
        area = math.pi * math.pow(radius,2)
        self.label.setText(f'Area = {area}')
        self.reset()

    def rectangle_click(self) -> None:
        """enables calculation criteria input boxes
                for a rectangle"""
        self.reset()
        self.label_input1.show()
        self.label_input1.setText('Length')
        self.inputText1.show()
        self.inputText1.setText('')
        self.label_input2.show()
        self.label_input2.setText('Width')
        self.inputText2.show()
        self.inputText2.setText('')
        self.buttonSubmit2.show()

    def rectangle_area(self) -> None:
        """calculates the area of rectangle"""
        length = float(self.inputText1.text())
        width = float(self.inputText2.text())
        self.label.setText(f'Area = {length * width}')
        self.reset()

    def triangle_click(self) -> None:
        """enables calculation criteria input boxes
                for a triangle"""
        self.reset()
        self.label_input1.show()
        self.label_input1.setText('Base')
        self.inputText1.show()
        self.inputText1.setText('')
        self.label_input2.show()
        self.label_input2.setText('Height')
        self.inputText2.show()
        self.inputText2.setText('')
        self.buttonSubmit2.show()

    def triangle_area(self) -> None:
        """calculates the area of triangle"""
        base = float(self.inputText1.text())
        height = float(self.inputText2.text())
        self.label.setText(f'Area = {(1/2) * base * height}')
        self.reset()

    def sphere_click(self) -> None:
        """enables calculation criteria input boxes
                for a sphere"""
        self.reset()
        self.label_input1.show()
        self.label_input1.setText('Radius')
        self.inputText1.show()
        self.inputText1.setText('')
        self.buttonSubmit1.show()

    def sphere_vol(self) -> None:
        """calculates the volume of a sphere"""
        radius = float(self.inputText1.text())
        self.label.setText(f'Volume = {(4/3) * math.pi * math.pow(radius, 3)}')
        self.reset()

    def cube_click(self) -> None:
        """enables calculation criteria input boxes
                for a cube"""
        self.reset()
        self.label_input1.show()
        self.label_input1.setText('Length')
        self.inputText1.show()
        self.inputText1.setText('')

        self.label_input2.show()
        self.label_input2.setText('Width')
        self.inputText2.show()
        self.inputText2.setText('')

        self.label_input3.show()
        self.label_input3.setText('Height')
        self.inputText3.show()
        self.inputText3.setText('')

        self.buttonSubmit3.show()

    def cube_vol(self) -> None:
        """calculates the volume of a cube"""
        length = float(self.inputText1.text())
        width = float(self.inputText2.text())
        height = float(self.inputText3.text())
        self.label.setText(f'Volume = {length * width * height}')
        self.reset()

    def cone_click(self) -> None:
        """enables calculation criteria input boxes
                for a cone"""
        self.reset()
        self.label_input1.show()
        self.label_input1.setText('Radius')
        self.inputText1.show()
        self.inputText1.setText('')
        self.buttonSubmit1.hide()

        self.label_input2.show()
        self.label_input2.setText('Height')
        self.inputText2.show()
        self.inputText2.setText('')
        self.buttonSubmit2.show()

    def cone_vol(self) -> None:
        """calculates the volume of a cone"""
        radius = float(self.inputText1.text())
        height = float(self.inputText2.text())
        self.label.setText(f'Volume = {(1/3) * math.pi * height * math.pow(radius, 2)}')
        self.reset()

    def submit1(self) -> None:
        """uses the input for the appropriately displayed
        text boxes and calls the associated function for
        calculation"""
        if self.radio_circle.isChecked():
            self.circle_area()
        elif self.radio_sphere.isChecked():
            self.sphere_vol()

    def submit2(self) -> None:
        """uses the input for the appropriately displayed
        text boxes and calls the associated function for calculation"""
        if self.radio_rectangle.isChecked():
            self.rectangle_area()
        elif self.radio_triangle.isChecked():
            self.triangle_area()
        elif self.radio_cone.isChecked():
            self.cone_vol()

    def submit3(self) -> None:
        """uses the input for the appropriately displayed
        text boxes and calls the cube volume calculation function"""
        self.cube_vol()
