from Programas.openGLUtils import OpenGLUtils
from Programas.base import Base
from Programas.attribute import Attribute
from OpenGL.GL import *


# Render a custom shape similar to the lion using lines
class Test(Base):
    def initialize(self):
        print("Initializing program...")

        ### Initialize program ###
        vsCode = """
        in vec3 position;
        void main()
        {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
        }
        """
        fsCode = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 1.0, 1.0);
        }
        """
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        ### Render settings (optional) ###
        glLineWidth(2)

        ### Set up vertex array object ###
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        ### Set up vertex attribute ###
        positionData = [[-0.025, 0.05, 0.0],  # Vertex 1
                        [-0.1, 0.125, 0.0],  # Vertex 2
                        [-0.175, 0.1, 0.0],  # Vertex 3
                        [-0.175, 0.00, 0.0],  # Vertex 4
                        [-0.1, -0.05, 0.0],  # Vertex 5
                        [-0.1, -0.1, 0.0],  # Vertex 6
                        [0.0, -0.125, 0.0],  # Vertex 7
                        [0.1, -0.1, 0.0],  # Vertex 8
                        [0.1, -0.05, 0.0],  # Vertex 9
                        [0.175, 0.00, 0.0],  # Vertex 10
                        [0.175, 0.1, 0.0],  # Vertex 11
                        [0.1, 0.125, 0.0],  # Vertex 12
                        [0.025, 0.05, 0.0]]  # Vertex 13

        positionData1 = [[-0.025, 0.05, 0.0],  # Vertex 1
                         [-0.1, 0.125, 0.0],  # Vertex 2
                         [-0.175, 0.1, 0.0],  # Vertex 3
                         [-0.225, 0.175, 0.0],  # Vertex 4
                         [-0.25, 0.35, 0.0],  # Vertex 5
                         [-0.125, 0.5, 0.0],  # Vertex 6
                         [-0.0, 0.425, 0.0],  # Vertex 7
                         [0.125, 0.5, 0.0],  # Vertex 8
                         [0.25, 0.35, 0.0],  # Vertex 9
                         [0.225, 0.175, 0.0],  # Vertex 10
                         [0.175, 0.1, 0.0],  # Vertex 11
                         [0.1, 0.125, 0.0],  # Vertex 12
                        [0.025, 0.05, 0.0]]  # Vertex 13


        self.vertexCount = len(positionData + positionData1)
        positionAttribute = Attribute("vec3", positionData + positionData1)
        positionAttribute.associateVariable(self.programRef, "position")

    def update(self):
        glUseProgram(self.programRef)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertexCount)


# Instantiate this class and run the program
Test().run()
