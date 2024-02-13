import { gql } from '@apollo/client';

export interface AddItemVariables {
  id: string;
  name: string;
  files: File[];
}

export interface AddItemResponse {
  addItem: {
    id: string;
    name: string;
    files: string[];
  };
}

export const ADD_ITEM = gql`
  mutation AddItem($id: String!, $name: String!, $files: [Upload!]!) {
    addItem(id: $id, name: $name, files: $files) {
      id
      name
      files
    }
  }
`;
