import yaml
import os
from xml.dom.minidom import Document

class DiagramSpec:
    def __init__(self, spec_dict):
        self.id = spec_dict.get('id')
        self.title = spec_dict.get('title')
        self.axes = spec_dict.get('axes', {})
        self.curves = spec_dict.get('curves', [])
        self.arrows = spec_dict.get('arrows', [])
        self.equilibrium = spec_dict.get('equilibrium', [])
        self.labels = spec_dict.get('labels', [])
        self.constraints = spec_dict.get('constraints', {})

class DiagramEngine:
    def generate(self, spec: DiagramSpec) -> str:
        # Create SVG document
        doc = Document()
        svg = doc.createElement('svg')
        svg.setAttribute('xmlns', 'http://www.w3.org/2000/svg')
        svg.setAttribute('width', '800')
        svg.setAttribute('height', '600')
        svg.setAttribute('viewBox', '0 0 800 600')
        doc.appendChild(svg)
        
        # Add title
        title = doc.createElement('text')
        title.setAttribute('x', '400')
        title.setAttribute('y', '50')
        title.setAttribute('text-anchor', 'middle')
        title.setAttribute('font-size', '20')
        title.setAttribute('font-family', 'Arial')
        title.appendChild(doc.createTextNode(spec.title))
        svg.appendChild(title)
        
        # Add axes
        x_axis = doc.createElement('line')
        x_axis.setAttribute('x1', '100')
        x_axis.setAttribute('y1', '500')
        x_axis.setAttribute('x2', '700')
        x_axis.setAttribute('y2', '500')
        x_axis.setAttribute('stroke', 'black')
        svg.appendChild(x_axis)
        
        y_axis = doc.createElement('line')
        y_axis.setAttribute('x1', '100')
        y_axis.setAttribute('y1', '100')
        y_axis.setAttribute('x2', '100')
        y_axis.setAttribute('y2', '500')
        y_axis.setAttribute('stroke', 'black')
        svg.appendChild(y_axis)
        
        # Add axis labels
        x_label = doc.createElement('text')
        x_label.setAttribute('x', '400')
        x_label.setAttribute('y', '540')
        x_label.setAttribute('text-anchor', 'middle')
        x_label.setAttribute('font-size', '14')
        x_label.setAttribute('font-family', 'Arial')
        x_label.appendChild(doc.createTextNode(spec.axes.get('x', '')))
        svg.appendChild(x_label)
        
        y_label = doc.createElement('text')
        y_label.setAttribute('x', '20')
        y_label.setAttribute('y', '300')
        y_label.setAttribute('text-anchor', 'middle')
        y_label.setAttribute('font-size', '14')
        y_label.setAttribute('font-family', 'Arial')
        y_label.setAttribute('transform', 'rotate(-90 20,300)')
        y_label.appendChild(doc.createTextNode(spec.axes.get('y', '')))
        svg.appendChild(y_label)
        
        # Add curves
        for curve in spec.curves:
            self._add_curve(doc, svg, curve)
            
        # Add arrows
        for arrow in spec.arrows:
            self._add_arrow(doc, svg, arrow)
            
        # Add equilibrium points
        for eq in spec.equilibrium:
            self._add_equilibrium_point(doc, svg, eq)
            
        # Add labels
        for label in spec.labels:
            self._add_label(doc, svg, label)
        
        # Add illustrative relationship text
        illustrative_text = doc.createElement('text')
        illustrative_text.setAttribute('x', '700')
        illustrative_text.setAttribute('y', '580')
        illustrative_text.setAttribute('text-anchor', 'end')
        illustrative_text.setAttribute('font-size', '12')
        illustrative_text.setAttribute('font-family', 'Arial')
        illustrative_text.appendChild(doc.createTextNode('Illustrative relationship'))
        svg.appendChild(illustrative_text)
        
        # Return the SVG as a properly formatted string without extra newlines
        return doc.toxml()
    
    def _add_curve(self, doc, svg, curve):
        # Create a simple linear curve for demonstration
        x1, y1 = 200, 400
        x2, y2 = 600, 200
        
        line = doc.createElement('line')
        line.setAttribute('x1', str(x1))
        line.setAttribute('y1', str(y1))
        line.setAttribute('x2', str(x2))
        line.setAttribute('y2', str(y2))
        
        if curve.get('style') == 'dashed':
            line.setAttribute('stroke-dasharray', '5,5')
            line.setAttribute('stroke', '#666666')
        else:
            line.setAttribute('stroke', 'black')
            
        line.setAttribute('stroke-width', '2')
        svg.appendChild(line)
        
        # Add label
        if curve.get('label'):
            label = doc.createElement('text')
            label.setAttribute('x', str(x2 + 10))
            label.setAttribute('y', str(y2 - 10))
            label.setAttribute('font-size', '12')
            label.setAttribute('font-family', 'Arial')
            label.appendChild(doc.createTextNode(curve.get('label')))
            svg.appendChild(label)
    
    def _add_arrow(self, doc, svg, arrow):
        # Simple arrow from one point to another
        x1, y1 = 300, 300
        x2, y2 = 400, 250
        
        line = doc.createElement('line')
        line.setAttribute('x1', str(x1))
        line.setAttribute('y1', str(y1))
        line.setAttribute('x2', str(x2))
        line.setAttribute('y2', str(y2))
        line.setAttribute('stroke', 'black')
        line.setAttribute('marker-end', 'url(#arrowhead)')
        svg.appendChild(line)
        
        # Add arrowhead definition
        defs = doc.createElement('defs')
        svg.appendChild(defs)
        
        marker = doc.createElement('marker')
        marker.setAttribute('id', 'arrowhead')
        marker.setAttribute('markerWidth', '10')
        marker.setAttribute('markerHeight', '7')
        marker.setAttribute('refX', '0')
        marker.setAttribute('refY', '3.5')
        marker.setAttribute('orient', 'auto')
        
        polygon = doc.createElement('polygon')
        polygon.setAttribute('points', '0 0, 10 3.5, 0 7')
        polygon.setAttribute('fill', 'black')
        marker.appendChild(polygon)
        defs.appendChild(marker)
        
        # Add arrow label
        if arrow.get('label'):
            label = doc.createElement('text')
            label.setAttribute('x', str((x1 + x2) / 2))
            label.setAttribute('y', str((y1 + y2) / 2 - 10))
            label.setAttribute('font-size', '12')
            label.setAttribute('font-family', 'Arial')
            label.appendChild(doc.createTextNode(arrow.get('label')))
            svg.appendChild(label)
    
    def _add_equilibrium_point(self, doc, svg, eq):
        # Draw equilibrium point as a circle
        x, y = 400, 300
        
        circle = doc.createElement('circle')
        circle.setAttribute('cx', str(x))
        circle.setAttribute('cy', str(y))
        circle.setAttribute('r', '5')
        
        if eq.get('style') == 'filled':
            circle.setAttribute('fill', 'black')
        else:
            circle.setAttribute('fill', 'white')
            circle.setAttribute('stroke', 'black')
            circle.setAttribute('stroke-width', '1')
            
        svg.appendChild(circle)
        
        # Add label
        if eq.get('label'):
            label = doc.createElement('text')
            label.setAttribute('x', str(x + 10))
            label.setAttribute('y', str(y - 10))
            label.setAttribute('font-size', '12')
            label.setAttribute('font-family', 'Arial')
            label.appendChild(doc.createTextNode(eq.get('label')))
            svg.appendChild(label)
    
    def _add_label(self, doc, svg, label):
        # Add custom text label
        text = doc.createElement('text')
        position = label.get('position', {})
        if isinstance(position, dict):
            x = position.get('x', 100)
            y = position.get('y', 100)
        else:
            # Handle case where position might be a string or other format
            x = 100
            y = 100
            
        text.setAttribute('x', str(x))
        text.setAttribute('y', str(y))
        text.setAttribute('font-size', '12')
        text.setAttribute('font-family', 'Arial')
        text.appendChild(doc.createTextNode(label.get('text', '')))
        svg.appendChild(text)

class SupplySideDiagram(DiagramEngine):
    """Supply-side economics diagram generator that extends DiagramEngine with specific functionality."""
    
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        
    def create_supply_demand_diagram(self, title, demand_curve_points, supply_curve_points, 
                                   equilibrium_point, shifted_demand=None, shift_direction=None):
        """Create a standard supply-demand diagram with proper visual conventions."""
        
        # Create spec dictionary for the diagram
        spec_dict = {
            'title': title,
            'axes': {'x': 'Quantity', 'y': 'Price'},
            'curves': []
        }
        
        # Add demand curve (solid, prominent)
        demand_curve = {
            'points': demand_curve_points,
            'style': 'solid',
            'color': 'blue',
            'label': 'D'
        }
        spec_dict['curves'].append(demand_curve)
        
        # Add original supply curve (dashed, subdued)
        supply_curve = {
            'points': supply_curve_points,
            'style': 'dashed',
            'color': 'red',
            'label': 'S'
        }
        spec_dict['curves'].append(supply_curve)
        
        # Add shifted demand if provided
        if shifted_demand:
            shifted_demand_curve = {
                'points': shifted_demand,
                'style': 'solid',
                'color': 'blue',
                'label': 'D\''
            }
            spec_dict['curves'].append(shifted_demand_curve)
        
        # Create diagram spec
        spec = DiagramSpec(spec_dict)
        
        # Generate the SVG
        svg_content = self.generate(spec)
        
        return svg_content
    
    def generate_diagram(self, spec_dict):
        """Generate a diagram from a specification dictionary."""
        spec = DiagramSpec(spec_dict)
        return self.generate(spec)