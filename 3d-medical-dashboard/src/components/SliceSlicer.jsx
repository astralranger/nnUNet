import React from 'react';

const SliceSlicer = ({ organName, sliceIndex, setSliceIndex, totalSlices = 15 }) => {
  return (
    <div className="slicer-panel">
      <div className="slicer-preview">
        <div style={{ width: '100%', height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#64748b', fontSize: '10px' }}>
             <img 
               key={`${organName}-${sliceIndex}`}
               src={`/models/slices/${organName.toLowerCase()}_${sliceIndex}.png`} 
               alt="Scan Slice" 
               style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }}
             />
             <div style={{ position: 'absolute', top: 10, left: 10, background: 'rgba(255,255,255,0.8)', color: '#1e293b', padding: '4px 8px', borderRadius: '6px', fontSize: '10px', fontWeight: 700, boxShadow: '0 2px 5px rgba(0,0,0,0.1)' }}>
                SLICE {sliceIndex + 1} / {totalSlices}
             </div>
        </div>
      </div>
      <div className="slicer-info">
        <div className="slicer-label">Cross-Sectional Scan Viewer (MRI/CT)</div>
        <div style={{ fontSize: '1.1rem', fontWeight: 700, margin: '0.2rem 0' }}>{organName} Scan Navigation</div>
        <p style={{ fontSize: '0.8rem', color: '#64748b' }}>Scrub through the volumetric data to see the segmentations on original image slices.</p>
        
        <input 
          type="range" 
          className="slice-slider" 
          min="0" 
          max={totalSlices - 1} 
          value={sliceIndex} 
          onChange={(e) => setSliceIndex(parseInt(e.target.value))}
        />
        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.7rem', color: '#94a3b8', marginTop: '0.5rem' }}>
          <span>Post-Inference Reconstruction</span>
          <span>Index: {sliceIndex} / {totalSlices}</span>
        </div>
      </div>
    </div>
  );
};

export default SliceSlicer;
