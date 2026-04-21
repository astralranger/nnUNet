import React, { useMemo } from 'react';
import * as THREE from 'three';

const OrganModel = ({ meshData, color = "#3b82f6", wireframe = false, opacity = 1.0, position = [0, 0, 0], scale = 1.0 }) => {
  const geometry = useMemo(() => {
    if (!meshData) return null;
    
    const geo = new THREE.BufferGeometry();
    const vertices = new Float32Array(meshData.vertices);
    const faces = new Uint32Array(meshData.faces);
    
    geo.setAttribute('position', new THREE.BufferAttribute(vertices, 3));
    geo.setIndex(new THREE.BufferAttribute(faces, 1));
    geo.computeVertexNormals();
    
    return geo;
  }, [meshData]);

  if (!geometry) return null;

  return (
    <mesh geometry={geometry} position={position} scale={scale}>
      <meshPhysicalMaterial 
        color={color}
        emissive={color}
        emissiveIntensity={0.5}
        roughness={0.1}
        metalness={0.9}
        transmission={0.6}
        thickness={1.5}
        transparent={true}
        opacity={opacity}
        wireframe={wireframe}
        side={THREE.DoubleSide}
        ior={1.5}
        envMapIntensity={1.5}
      />
    </mesh>
  );
};

export default OrganModel;
