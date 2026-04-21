import React, { useState, useEffect, Suspense } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, PerspectiveCamera, Environment, Float, ContactShadows, Stars } from '@react-three/drei';
import { Activity, Heart, Brain, Scissors, Focus, Maximize, Settings2, Info, User, Layers, ScanLine } from 'lucide-react';
import OrganModel from './components/OrganModel';
import HumanBody from './components/HumanBody';
import SliceSlicer from './components/SliceSlicer';

const ORGANS = [
  { id: 'heart', name: 'Heart', icon: Heart, color: '#e11d48', label: 'Left Atrium', pos: [-0.08, 0.35, 0.1], scale: 0.15, accuracy: '89.5%' },
  { id: 'spleen', name: 'Spleen', icon: Scissors, color: '#059669', label: 'Splenic Tissue', pos: [0.15, 0.2, 0.0], scale: 0.2, accuracy: '93.2%' },
  { id: 'prostate', name: 'Prostate', icon: Focus, color: '#d97706', label: 'Prostate Gland', pos: [0, -0.35, 0.05], scale: 0.12, accuracy: '84.8%' },
  { id: 'hippocampus', name: 'Hippocampus', icon: Brain, color: '#7c3aed', label: 'CA1/CA3 Regions', pos: [0, 0.9, 0.02], scale: 0.1, accuracy: '91.0%' },
];

function App() {
  const [selectedOrgan, setSelectedOrgan] = useState(ORGANS[1]);
  const [allMeshData, setAllMeshData] = useState({});
  const [loading, setLoading] = useState(true);
  const [wireframe, setWireframe] = useState(false);
  const [autoRotate, setAutoRotate] = useState(true);
  const [viewMode, setViewMode] = useState('body'); // 'body' or 'focus'
  const [sliceIndex, setSliceIndex] = useState(5);
  const [morphologyEnabled, setMorphologyEnabled] = useState(true);

  useEffect(() => {
    async function loadAllMeshes() {
      setLoading(true);
      const data = {};
      try {
        await Promise.all(ORGANS.map(async (organ) => {
          // All organs use refined by default in body view
          const res = await fetch(`./models/${organ.id}.json`);
          data[organ.id] = await res.json();
        }));
        setAllMeshData(data);
      } catch (err) {
        console.error("Failed to load models:", err);
      } finally {
        setLoading(false);
      }
    }
    loadAllMeshes();
  }, []);

  // Effect to handle the Raw vs Refined toggle for the selected organ
  useEffect(() => {
    if (viewMode === 'focus') {
      async function reloadModel() {
        const fileSuffix = (!morphologyEnabled && selectedOrgan.id === 'spleen') ? '_raw' : '';
        try {
          const res = await fetch(`./models/${selectedOrgan.id}${fileSuffix}.json`);
          const mesh = await res.json();
          setAllMeshData(prev => ({ ...prev, [selectedOrgan.id]: mesh }));
        } catch (err) {
            console.error("Failed to toggle morphology:", err);
        }
      }
      reloadModel();
    }
  }, [morphologyEnabled, selectedOrgan, viewMode]);

  return (
    <div className="dashboard-container">
      <aside className="sidebar">
        <div>
          <h1>MED<span>-AI</span> 3D</h1>
          <p className="tagline">Anatomical Digital Twin</p>
        </div>

        <nav className="organ-selector">
          <button 
            className={`organ-btn ${viewMode === 'body' ? 'active' : ''}`}
            onClick={() => setViewMode('body')}
            style={{ marginBottom: '1rem' }}
          >
            <User size={20} />
            <span style={{ fontWeight: 700 }}>Full Body Analysis</span>
          </button>

          <p style={{ fontSize: '0.7rem', color: '#64748b', marginBottom: '0.5rem', fontWeight: 600 }}>FOCUSED ORGANS</p>
          {ORGANS.map((organ) => (
            <button
              key={organ.id}
              className={`organ-btn ${selectedOrgan.id === organ.id && viewMode === 'focus' ? 'active' : ''}`}
              onClick={() => {
                setSelectedOrgan(organ);
                setViewMode('focus');
                setSliceIndex(5);
              }}
            >
              <organ.icon size={18} color={selectedOrgan.id === organ.id ? organ.color : '#64748b'} />
              <span>{organ.name}</span>
            </button>
          ))}
        </nav>

        <div className="metrics-card">
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem' }}>
            <Activity size={18} color="#059669" />
            <span style={{ fontSize: '0.875rem', fontWeight: 700 }}>Analysis Insights</span>
          </div>
          <div className="metric-item">
            <span className="metric-label">Mode</span>
            <span className="metric-value">{viewMode === 'body' ? 'Multi-Organ' : 'Focused Scan'}</span>
          </div>
          <div className="metric-item">
            <span className="metric-label">Resolution</span>
            <span className="metric-value">0.750 mm</span>
          </div>
          <div className="metric-item">
            <span className="metric-label">Mesh Accuracy</span>
            <span className="metric-value" style={{ color: '#2563eb' }}>
                {viewMode === 'body' ? 'Weighted Avg' : selectedOrgan.accuracy}
            </span>
          </div>
        </div>
      </aside>

      <main className="main-view">
        {loading && (
          <div className="loading-overlay">
            <div className="spinner"></div>
            <p style={{ color: '#64748b', fontSize: '0.875rem', fontWeight: 500 }}>Reconstructing Neural Volumes...</p>
          </div>
        )}

        <div className="canvas-container">
          <Canvas shadows>
            <PerspectiveCamera makeDefault position={[0, 0, viewMode === 'body' ? 3.5 : 2.5]} fov={50} />
            <color attach="background" args={['#f8fafc']} />
            
            <Suspense fallback={null}>
              <HumanBody />
              
              {viewMode === 'body' ? (
                ORGANS.map(organ => (
                  <OrganModel 
                    key={organ.id}
                    meshData={allMeshData[organ.id]} 
                    color={organ.color} 
                    wireframe={wireframe}
                    position={organ.pos}
                    scale={organ.scale}
                    opacity={0.7}
                  />
                ))
              ) : (
                <Float speed={2} rotationIntensity={0.5} floatIntensity={0.5}>
                  <OrganModel 
                    meshData={allMeshData[selectedOrgan.id]} 
                    color={selectedOrgan.color} 
                    wireframe={wireframe}
                    scale={0.8}
                  />
                </Float>
              )}
              
              <Environment preset="studio" />
              <ContactShadows opacity={0.1} scale={10} blur={2} far={4.5} />
              
              <spotLight position={[10, 10, 10]} angle={0.15} penumbra={1} intensity={1} />
              <pointLight position={[-10, 0, -10]} intensity={0.2} />
            </Suspense>

            <OrbitControls 
              enablePan={false} 
              autoRotate={autoRotate} 
              autoRotateSpeed={0.5}
              makeDefault
            />
          </Canvas>
        </div>

        {viewMode === 'focus' && (
          <SliceSlicer 
            organName={selectedOrgan.name} 
            sliceIndex={sliceIndex} 
            setSliceIndex={setSliceIndex} 
          />
        )}

        <div className="controls-overlay">
          <button 
            className={`control-btn ${morphologyEnabled ? 'active' : ''}`}
            onClick={() => setMorphologyEnabled(!morphologyEnabled)}
            title="Toggle Morphological Refinement"
          >
            <Activity size={18} color={morphologyEnabled ? 'white' : 'red'} />
          </button>
          <button 
            className={`control-btn ${viewMode === 'body' ? 'active' : ''}`}
            onClick={() => setViewMode(viewMode === 'body' ? 'focus' : 'body')}
            title="Toggle Body Context"
          >
            <Layers size={18} />
          </button>
          <button 
            className="control-btn" 
            onClick={() => setWireframe(!wireframe)}
            title="Toggle Wireframe"
          >
            <Maximize size={18} />
          </button>
          <button 
            className="control-btn" 
            onClick={() => setAutoRotate(!autoRotate)}
            title="Auto Rotate"
          >
            <Settings2 size={18} />
          </button>
        </div>
      </main>
    </div>
  );
}

export default App;
