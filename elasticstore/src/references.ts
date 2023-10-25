import { Reference } from "./types"

// Records should be added here to be indexed / made searchable
const references: Array<Reference> = [
  {
    collection: "users",
    index: "users",
    /* 
    mappings: {
      location: {
        type: "geo_point" // elasticsearch's definition of a geopoint
      }
    },
    transform: (data, parent) => ({
      ...data,
      location: `${data.location._latitude},${data.location._longitude}` // transform from firestore's geopoint to elasticsearch's
    })
    */
  }
]

export default references
