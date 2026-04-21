import React from 'react';
import { Capsule } from '@react-three/drei';

const HumanBody = () => {
  return (
    <group opacity={0.1}>
      {/* Torso */}
      <Capsule args={[0.4, 1.2, 4, 16]} position={[0, 0, 0]}>
        <meshPhysicalMaterial 
          color="#cbd5e1" 
          transparent 
          opacity={0.1} 
          roughness={1} 
          metalness={0}
          transmission={0.5}
          thickness={0.1}
          wireframe
        />
      </Capsule>
      
      {/* Head */}
      <mesh position={[0, 0.9, 0]}>
        <sphereGeometry args={[0.18, 16, 16]} />
        <meshPhysicalMaterial 
          color="#334155" 
          transparent 
          opacity={0.05} 
          wireframe
        />
      </mesh>
    </group>
  );
};

export default HumanBody;
